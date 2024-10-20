import sqlite3
conn = sqlite3.connect("database.db")
db = conn.cursor()

foods_to_insert = [
    ("Margherita", "Pizza", 12.50),
    ("Formaggio", "Pizza", 15.50),
    ("Chicken", "Pizza", 17.00),
    ("Pineapple'o'clock", "Pizza", 16.50),
    ("Meat Town", "Pizza", 20.00),
    ("Parma", "Pizza", 20.00),
    ("Lasagna", "Salads", 13.50),
    ("Ravioli", "Salads ", 14.50),
    ("Spaghetti Classics", "Salads", 11.00),
    ("Seafood pasta", "Salads ", 25.50),
    ("Today's Soup", "Starter", 5.50),
    ("Bruschetta", "Starter", 8.50),
    ("Garlic bread", "Starter", 9.50),
    ("Tomozzarella", "Starter", 10.50),
]

db.executemany("""
    INSERT INTO foods (name, category, price)
    VALUES (?, ?, ?)
""", foods_to_insert)

conn.commit()

conn.close()
