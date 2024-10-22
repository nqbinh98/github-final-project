# WEBSITE ORDER FOOD
#### Video Demo: [Watch here](https://youtu.be/g1v_U0chgKY)
#### Description:

This project is my final submission for CS50x, and it involves developing a fully functional food ordering website. The main goal of this project is to create a user-friendly platform where users can register, browse food options, place orders, and manage their accounts. Below are the primary features that this website offers:

User Registration: Users have the option to create an account by signing up with a unique username and password. The system ensures that each username is unique, and it also checks whether the provided password meets basic security standards.

Login and Logout: After registering, users can log in securely using their credentials. The login system checks the username and password against the database, where passwords are stored securely using hashing techniques to protect user information. Once logged in, users can browse food items and manage their orders. They can also log out anytime.

Food Ordering: Once users are logged in, they are presented with a list of available food items. Users can browse through different categories of food, choose the items they want, specify the quantity, and place orders. The total price is calculated based on the food item’s price and quantity.

Order Management: Users have access to an order history where they can review previous orders. This feature allows users to track what they have ordered, view details such as food items and the amounts, and check the total cost of each order.

Password Change: Users also have the option to change their password. This ensures that they can maintain account security by regularly updating their credentials if needed.

Technologies Used:

To implement the project, I used a combination of frontend and backend technologies to ensure smooth functionality and a seamless user experience:

Frontend: I used HTML, CSS, and JavaScript to design and implement the user interface. These technologies help create an interactive and responsive website.

HTML is used to structure the web pages, including the login page, registration page, homepage, and order history page.
CSS is used to style the pages and make the site visually appealing. The layout is clean and simple, ensuring ease of use.
JavaScript adds interactivity to the site, such as handling button clicks and updating the user interface dynamically.
Backend: The backend is built using Python and the Flask framework. Flask is a lightweight and easy-to-use web framework that allows for efficient routing, session management, and handling HTTP requests.

In app.py, I defined the routes and logic that power the website’s core functionality. It handles everything from logging in and registering to managing orders and handling password changes. Each function is linked to specific routes that users can visit or interact with.
Database: To store user data, food items, and orders, I used SQLite3. SQLite3 is a lightweight, serverless database system that integrates seamlessly with Flask. All the user information, food categories, and orders are stored in a single database file called Database.db. This file stores structured data in tables, which can be queried and updated as users interact with the website.

Key Components of the Website:

app.py:
This file serves as the backbone of the application. It contains all the essential Flask routes and logic.

Login Function: 
This function checks whether a user has entered a valid username and password in the login form. If the credentials match an existing user in the database, the user is logged in; otherwise, an error message is displayed.

Logout Function: 
This function allows users to log out of their account by clearing the session data. It helps protect user privacy by ensuring that after logging out, no one else can access their session.

Register Function: 
The registration function handles new user signups. It checks if a username already exists in the database. If not, it securely hashes the password and stores the new user’s credentials in the database.

Change Password Function: 
This function allows users to change their password. It checks that the old password matches the one stored in the database, and it ensures that the new password matches the confirmation before updating the database.

Buy Function: 
This function handles the food ordering process. It retrieves the selected food item, price, and quantity, calculates the total cost, and then saves the order to the orders table in the database.

Database.db:
This file stores the persistent data for the website. It contains multiple tables, including one for user accounts (users), one for food items (foods), and one for orders (orders). When a user registers, places an order, or changes their password, the corresponding information is updated in the database.

layout.html:
The layout template is used to provide a consistent design across all pages. It includes a navigation bar with links to various sections like Home, About, Contact, as well as buttons for logging out or registering. The layout ensures that each page maintains a similar structure for a better user experience.

helpers.py:
This file contains utility functions. One example is the login_required decorator, which ensures that users must log in before they can access certain features like placing orders. This file helps reduce redundancy by centralizing commonly used functions.

User Journey:
When you first visit the website, you are greeted with a login page. If you already have an account, you can log in to access the main features. If you don’t have an account, you can click on the "Register" button to create one. Once logged in, you can browse the available food items, select what you want to order, and place your order. You can also view your order history by clicking on the cart icon in the navigation bar. Additionally, you have the option to change your password at any time, ensuring that your account remains secure.

Feedback:
I hope you enjoy exploring my food ordering website! If you encounter any bugs or have suggestions for improvement, feel free to leave a comment. Your feedback will help me refine and enhance the project.
