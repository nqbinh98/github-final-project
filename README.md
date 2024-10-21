# YOUR PROJECT TITLE
#### Video Demo: [Watch here](https://youtu.be/g1v_U0chgKY)
<!-- <URL https://youtu.be/g1v_U0chgKY> -->
#### Description:

Description:
This is my final project for CS50x, where I developed a food ordering website. The main features of the site include:

User Registration: Users can create accounts to access the system.
Login and Logout: Users can log in and out securely.
Food Ordering: Once logged in, users can browse food categories, select items, specify quantities, and place orders.
Order Management: Users can view and manage their orders.
Password Change: Users have the ability to change their passwords.
I implemented the project using:

Frontend: HTML, CSS, and JavaScript.
Backend: Python and Flask to handle the core functionality.
Database: SQLite3 to store data for users, orders, and food items.
Key Components:
app.py: This is the main file where I used Flask to build the backend logic. It handles routes for user authentication (login, logout, registration, password change) and order management. I used SQLite3 to manage the database of user accounts, orders, and food items.

Database.db: This SQLite database stores all relevant data, including user information, food categories, and orders.

layout.html: This template sets up the basic layout for the site. Other pages (e.g., index, login, and logout) extend this layout to ensure a consistent structure.

helpers.py: This file contains utility functions, such as login_required, which ensures that users must log in before accessing certain features (like placing orders).

Feedback:
I hope you enjoy exploring the website! If you find any bugs or issues, feel free to leave a comment so I can address them.