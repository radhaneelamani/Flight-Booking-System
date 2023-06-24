# Flight Booking System
### Project Description
The flight booking system is a web-based application that allows users to search and book flights based on their travel requirements. The system provides a user-friendly interface for users to search for available flights, view flight details, and make reservations. It also includes an administrative interface for managing flights.
The main features of the flight booking system include:
- User:
    - User Registration:</br>
      Users can create an account to access personalised features and manage their bookings.
    - User Login:</br>
      The users are authenticated based on their registration details stored in the database.
    - Flight Search:</br>
      The users can specify their departure and arrival locations and the desired departure date. The system retrieves and displays a list of available flights matching the search criteria, showing details such as flight number, departure city, departure time, arrival city, arrival time, and available seats.
    - Flight Selection:</br>
      Users can select a flight from the search results and proceed to book their tickets.
    - Booking Process:</br>
      Users can book tickets by providing their personal information, including name, gender, phone number, and email address.
    - Booking Management:</br>
      Users can see view and manage their bookings, including viewing booking details and cancelling bookings.
    - View Booking History:</br>
      Users can access their booking history to review past and upcoming flights they have booked.
- Administrator:
    - Admin Login:</br>
      The credentials will be matched with the database and the admin login is authenticated.
    - Admin Dashboard:</br>
      An administrative interface that provides access to view current flights, manage flights and view bookings.
    - Flight Management:</br>
      Admins can add new flights, update flight details (departure/arrival locations, dates, times, etc.), and remove flights if necessary.
    - View Bookings:</br>
      Admins have the ability to view and manage user bookings according to the flight number, thereby having access to the details of passengers boarding a particular flight.
Whenever a user books or cancels a reservation the available seat count will be updated and shown to the other users booking the flight and to the admin.      

The Tech Stack used in this project is as follows:
- HTML, CSS, JavaScript, BootStrap : Front End
- Flask, Python : Back End
- Sqlite : Database    

Website Snapshots:
- Website Main Page:
  ![main page](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/93187a01-2cbd-484b-a25f-17d9990fb155)
- Admin Login:
  ![admin login](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/20757cbb-146c-4236-bc1e-65474883b18a)
- Admin Login Failed due to invalid credentials:
  ![admin login failed](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/70d04149-811d-4b27-93b4-13ebc451da26)
- Admin Home:
  ![admin home](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/1b9c01a7-847c-4ffe-bdd8-13d42c3d747c)
- Admin View Bookings of a particular flight( FN101):
  ![passenger details per flight](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/e46f04d0-08d5-427a-b955-9391d62f1c93)
- Admin Flight Management: Adding a new Flight:
  ![addflights](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/ab84bcc6-dd6b-4294-89c8-414fa89a9c3f)
- New flight successfully added:
  ![new flight added](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/2a294fbe-9156-4b91-abd5-7a18e1eab977)
- Admin Flight Management: Removing flight:
  ![remove flights](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/1f7c32cb-d602-4816-9606-e69f13743469)
- Flight removed successfully:
  ![flight removed](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/6c42b836-40fe-4a06-ab9c-08898f11d0a6)
- User Signup:
  ![user signup](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/7785a48e-40ef-4a9a-8aba-19c82dc6626d)
- User Login:
  ![user login](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/a3da8dd2-ea03-49bd-9aeb-501671109dae)
- User Home: Flight Search:
  ![user home](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/80bce0d1-40d3-4f22-a691-988272ebad6c)
- Flight Search Results/ Select flight:
  ![search results](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/d588543c-4f52-41bf-9f46-4b16ed32a2aa)
- Booking a ticket:
  ![ticket booking](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/f7710523-fd20-4acf-b1ac-11d31c9ee075)
- Booking Successful:
  ![booking successful](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/6accc243-d3d8-4a3c-a251-e69dfa3ab859)
- View Booking History, Cancel Booking:
  ![mybooking](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/5fd99921-5b3f-4300-b5ce-a454592396dc)
- Updation of available seats on the admin side due to a new booking:
  ![updated seats admin side after booking](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/b19fbe5f-43ac-4de5-ac93-8e1114499f90)
- New passenger details for FN101:
  ![new passenger addedd](https://github.com/radhaneelamani/Flight-Booking-System/assets/105295708/0d9d5f40-daf5-4c2e-80a4-d0e36c136071)
