import os

from flask_session import Session
from flask import Flask, flash, render_template, request, redirect, url_for, session
from helpers import apology, login_required, usd
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.jinja_env.filters["usd"] = usd
db = SQL("sqlite:///database.db")

db.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
""")
db.execute("""
    CREATE TABLE IF NOT EXISTS foods (
        id_food INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL
);
""")
db.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id_order INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        id_user INTEGER NOT NULL,
        pay REAL NOT NULL,
        FOREIGN KEY (id_user) REFERENCES users(id)
);
""")

if __name__ == '__main__':
    app.run(debug=True)

# @app.route("/", methods=["GET", "POST"])
@app.route("/")
@login_required
def index():
    if request.method == "POST":
        result = buy()  # Gọi hàm xử lý logic "buy"
        if result:  # Giả sử bạn trả về kết quả thành công hoặc thất bại
            flash("Order placed successfully!", "success")
        else:
            flash("Failed to place order!", "error")
    return render_template("index.html")




@app.route('/login', methods=['GET', 'POST'])
def login():

    # Forget any user_id
    session.clear()

    if request.method == "POST":

        if not request.form.get("username"):
            return apology("Must provide username", 403)
        if not request.form.get("password"):
            return apology("Must provide password", 403)
        
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get('username')
        )
        
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            return apology("Invalid username and/or password", 403)
        
        session["user_id"] = rows[0]["id"]

        return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("index"))


@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():
    currentId = session["user_id"]

    if request.method == "POST":
        newPass = request.form.get("newpassword")
        oldPass = request.form.get("password")
        confirm = request.form.get("confirmation")
        print(oldPass)
        print(newPass)
        print(confirm)

        if not oldPass:
            return apology("Must provide password", 403)
        
        get_hash_pass = db.execute("SELECT password FROM users WHERE id = ?", currentId)
        hash_pass = get_hash_pass[0]["password"]

        if not check_password_hash(hash_pass, oldPass):
            return apology("Password incorrect", 403)

        if not newPass:
            return apology("Must provide new password", 403)        

        if not confirm:
            return apology("Must provide confirm password", 403)        
        
        if confirm != newPass:
            return apology("Confirm password do not match", 403)        

        update_password = generate_password_hash(newPass)
        db.execute("UPDATE users SET password = ? WHERE id = ?", update_password, currentId)

        return redirect(url_for('index'))
    else:
        return render_template("changepass.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Check input username
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            return apology("Must provide username", 400)

        # Check username is already have in table
        table_exists = db.execute(
            """SELECT name FROM sqlite_master WHERE type='table' AND name='users';"""
        )
        

        if table_exists:
            checkUsername = db.execute("SELECT * FROM users WHERE username = ?",
            username) 

            if len(checkUsername) != 0:
                return apology("Username already exists", 400)

            password = request.form.get("password")    
            if not password:
                return apology("Missing password", 400)
            
            confirmation = request.form.get("confirmation")    
            if not confirmation:
                return apology("Missing confirmation password", 400)
            if confirmation != password:
                return apology("Confirmation do not match", 400)

            # Insert username and password
            hashed_password = generate_password_hash(password)
            db.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                        username, hashed_password)
            getId = db.execute("SELECT id FROM users WHERE username = ?", username)
            userId = getId[0]["id"]
            session["user_id"] = userId

            flash("Registered!")
        return redirect(url_for('index'))
    else:
        return render_template("register.html")
    
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():

    currentId = session["user_id"]

    if request.method == "POST":
        category = request.form.get("category")
        food = request.form.get("food")
        amount = request.form.get("amount")
        
        if not category or not food or not amount:
            return apology("must provide infomation to buy", 400)
        
        try:
            amount = int(amount)
            if amount <=0:
                return apology("Amount must be positive integer", 400)
        except ValueError:
            return apology("Amount must be an integer", 400)
            
        table_food = db.execute(
            """SELECT name FROM sqlite_master WHERE type='table' AND name='foods';"""
        )
        if table_food:
            price = db.execute(
                """SELECT price FROM foods WHERE name = ?""", food
            )
            money = price[0]["price"]
            bill = money * amount
            db.execute(
                """ INSERT INTO orders (name, id_user, pay) VALUES (?, ?, ?)""",
                food, currentId, bill
            )
            return redirect("/")
    else:
        return render_template("index.html")
 


@app.route("/orders")
@login_required
def orders():
    currentId = session["user_id"]

    trans = db.execute("""SELECT * FROM orders WHERE id_user = ?""", currentId)
    return render_template("orders.html", trans=trans)
    
