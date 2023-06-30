from flask import Blueprint, render_template, request, redirect
import sqlite3

admin_routes = Blueprint('admin', __name__)


@admin_routes.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    error_message = None
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']

        # Connect to the SQLite database
        conn = sqlite3.connect('flightreservationdb.db')
        cursor = conn.cursor()

        # Retrieve the admin information from the admindetails table
        cursor.execute("SELECT * FROM admindetails WHERE username = ? AND password = ?", (username, password))
        admin = cursor.fetchone()

        if admin:
            # Admin login successful
            # Implement admin authentication logic here
            conn.close()
            return redirect('/admin/home')  # Redirect to the admin home page
        else:
            # Admin login failed
            conn.close()
            error_message = "Invalid credentials. Please try again."

    return render_template('/admin/login.html', error_message=error_message)


@admin_routes.route('/logout', methods=['GET'])
def logout():
    return redirect('/')


@admin_routes.route('/admin/home')
def admin_home():
    # Connect to the SQLite database
    conn = sqlite3.connect('flightreservationdb.db')
    cursor = conn.cursor()

    # Retrieve the current flights from the flights table
    cursor.execute("SELECT * FROM flights")
    flights = cursor.fetchall()

    conn.close()

    return render_template('/admin/home.html', flights=flights)


# Add Flight route
@admin_routes.route('/admin/addflight', methods=['GET', 'POST'])
def add_flight():
    if request.method == 'POST':
        # Get flight details from the form
        flight_number = request.form['flight_number']
        departure_city = request.form['departure_city']
        departure_date = request.form['departure_date']
        departure_time = request.form['departure_time']
        arrival_city = request.form['arrival_city']
        arrival_date = request.form['arrival_date']
        arrival_time = request.form['arrival_time']
        available_seats = request.form['available_seats']

        # Connect to the SQLite database
        conn = sqlite3.connect('flightreservationdb.db')
        cursor = conn.cursor()

        # Insert flight details into the database
        cursor.execute(
            "INSERT INTO flights "
            "(flight_number, departure_city, departure_date, departure_time, "
            "arrival_city, arrival_date, arrival_time, available_seats) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (flight_number, departure_city, departure_date, departure_time,
             arrival_city, arrival_date, arrival_time, available_seats))
        conn.commit()
        return redirect('/admin/home')
    return render_template('/admin/addflight.html')

    # return redirect('/admin/home')


# Remove Flight route
@admin_routes.route('/admin/removeflight', methods=['GET', 'POST'])
def remove_flight():
    if request.method == 'POST':
        # Get flight ID from the form
        flight_number = request.form['flight_number']

        # Connect to the SQLite database
        conn = sqlite3.connect('flightreservationdb.db')
        cursor = conn.cursor()

        # Delete flight from the database
        cursor.execute("DELETE FROM flights WHERE flight_number = ?", (flight_number,))
        conn.commit()
        return redirect('/admin/home')

    return render_template('/admin/removeflight.html')


@admin_routes.route('/admin/passengerdetails/<flight_number>')
def passenger_details(flight_number):
    # Connect to the SQLite database
    conn = sqlite3.connect('flightreservationdb.db')
    cursor = conn.cursor()

    # Retrieve the passenger details from the bookings table
    cursor.execute("SELECT * FROM bookings WHERE flight_number = ?", (flight_number,))
    passengers = cursor.fetchall()

    conn.close()

    return render_template('/admin/passengerdetails.html', passengers=passengers, flight_number=flight_number)
