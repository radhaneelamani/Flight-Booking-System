from flask import Blueprint, render_template, request, redirect, flash, session
import sqlite3

user_routes = Blueprint('user', __name__)

user_routes.secret_key = 'session_key'


@user_routes.route('/user/login', methods=['GET', 'POST'])
def user_login():
    error_message = None
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']

        # Connect to the SQLite database
        conn = sqlite3.connect('flightreservationdb.db')
        cursor = conn.cursor()

        # Retrieve the user information from the users table
        cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            # User login successful
            # Implement user authentication logic here
            session['username'] = username
            conn.close()
            return redirect('/user/home')  # Redirect to the user home page
        else:
            # Admin login failed
            conn.close()
            error_message = "Invalid credentials. Please try again."

    return render_template('/user/login.html', error_message=error_message)


# Add new user
@user_routes.route('/user/signup', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Get user details from the form
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phonenumber = request.form['phonenumber']

        # Connect to the SQLite database
        conn = sqlite3.connect('flightreservationdb.db')
        cursor = conn.cursor()

        # Insert flight details into the database
        cursor.execute(
            "INSERT INTO users "
            "(username, password, email, phonenumber)"
            "VALUES (?,?,?,?)",
            (username, password, email, phonenumber))
        conn.commit()
        return redirect('/user/login')
    return render_template('/user/signup.html')


@user_routes.route('/logout', methods=['GET'])
def logout():
    return redirect('/')


@user_routes.route('/user/home')
def user_home():
    return render_template('/user/home.html')


@user_routes.route('/searchflights', methods=['POST'])
def search_flights():
    if request.method == 'POST':
        # Retrieve the form data
        from_location = request.form['from_location']
        to_location = request.form['to_location']
        departure_date = request.form['departure_date']

        # Connect to the SQLite database
        conn = sqlite3.connect('flightreservationdb.db')
        cursor = conn.cursor()

        # Retrieve the flights based on the form inputs
        cursor.execute("SELECT * FROM flights WHERE departure_city = ? AND arrival_city = ? AND departure_date = ?",
                       (from_location, to_location, departure_date))
        flights = cursor.fetchall()
        if flights:
            # Close the database connection
            conn.close()

            # Render the flights.html template with the retrieved flights
            return render_template('/user/flights.html', flights=flights)
        else:
            conn.close()
            # error_message = "No flights found"
            return render_template('/user/home.html')
    # Redirect to the user home page if the request method is not POST

    return redirect('/user/home')


@user_routes.route('/user/bookticket/<flight_number>', methods=['GET', 'POST'])
def book_ticket(flight_number):
    if request.method == 'POST':
        # Get the form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        phone_number = request.form['phone_number']
        email = request.form['email']
        flight_id = request.form['flight_id']
        username = session.get('username')
        print(session['username'])

        # Connect to the SQLite database
        conn = sqlite3.connect('flightreservationdb.db')
        cursor = conn.cursor()

        # Insert booking details into the bookings table
        cursor.execute(
            "INSERT INTO bookings "
            "(first_name, last_name, gender, phone_number, email_id, flight_id, flight_number, username)"
            "VALUES (?,?,?,?,?,?,?,?)",
            (first_name, last_name, gender, phone_number, email, flight_id, flight_number, username))
        conn.commit()

        # Update the available seats count in the flights table
        cursor.execute("UPDATE flights SET available_seats = available_seats - 1 WHERE flight_id = ?", (flight_id,))
        conn.commit()

        cursor.execute("SELECT * FROM flights WHERE flight_number = ?", (flight_number,))
        flights = cursor.fetchone()
        cursor.execute("SELECT * FROM bookings WHERE flight_number = ? AND username = ?", (flight_number, username))
        bookings = cursor.fetchone()

        conn.close()

        flash('Ticket booked successfully!', 'success')
        return render_template('/user/bookingsuccessful.html', booking=bookings, flight=flights)

    # Retrieve the flight details from the flights table
    conn = sqlite3.connect('flightreservationdb.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flights WHERE flight_number = ?", (flight_number,))
    flight = cursor.fetchone()
    conn.close()

    return render_template('/user/bookticket.html', flight=flight)


@user_routes.route('/mybookings')
def my_bookings():
    # Get the logged-in user's ID or username from the session
    username = session.get('username')
    print(username)
    # username = 'tomh'  # For testing purposes

    # Connect to the SQLite database
    conn = sqlite3.connect('flightreservationdb.db')
    cursor = conn.cursor()

    # Retrieve the bookings for the logged-in user from the bookings table
    cursor.execute("SELECT * FROM bookings WHERE username = ?", (username,))
    bookings = cursor.fetchall()

    conn.close()

    return render_template('/user/mybookings.html', bookings=bookings)


@user_routes.route('/user/cancelticket/<booking_id>', methods=['POST'])
def cancel_ticket(booking_id):
    # Connect to the SQLite database
    conn = sqlite3.connect('flightreservationdb.db')
    cursor = conn.cursor()

    # Retrieve the flight ID associated with the booking
    cursor.execute("SELECT flight_id FROM bookings WHERE booking_id = ?", (booking_id,))
    flight_id = cursor.fetchone()[0]

    # Delete the booking from the database
    cursor.execute("DELETE FROM bookings WHERE booking_id = ?", (booking_id,))
    conn.commit()

    # Update the available seats count in the flights table
    cursor.execute("UPDATE flights SET available_seats = available_seats + 1 WHERE flight_id = ?", (flight_id,))
    conn.commit()

    conn.close()

    # Flash a success message
    flash('Ticket canceled successfully!', 'success')

    return redirect('/mybookings')  # Redirect to the updated bookings page
