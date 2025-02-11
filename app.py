from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session and flashing messages

# Database setup
DATABASE = 'database.db'

# Create the database tables (run this once)
def create_tables():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
    """)
    # User health table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_health (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        height REAL,
        weight REAL,
        age INTEGER,
        gender TEXT,
        activity_level TEXT,
        bmi REAL,
        health_status TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    conn.commit()
    conn.close()

create_tables()

def create_food_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Table to store food options for each user
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_food (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        day TEXT,
        meal TEXT,
        food TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """)
    conn.commit()
    conn.close()

create_food_table()


# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hash_password(password)

        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
            conn.commit()
            conn.close()
            flash("Signup successful! Please log in.", "success")
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Username already exists. Try a different one.", "danger")
    return render_template('signup.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = hash_password(password)

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, password_hash))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user_id"] = user[0]  # Save the user ID in the session
            flash("Login successful! Welcome, " + username, "success")
            return redirect(url_for('bmi'))
        else:
            flash("Invalid username or password. Try again.", "danger")

    return render_template('login.html')

# BMI calculation route
@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    if "user_id" not in session:  # Ensure the user is logged in
        flash("Please log in to access this page.", "danger")
        return redirect(url_for("login"))

    if request.method == "POST":
        user_id = session["user_id"]  # Retrieve logged-in user ID
        height = float(request.form["height"]) / 100  # Convert cm to meters
        weight = float(request.form["weight"])
        age = int(request.form["age"])
        gender = request.form["gender"]
        activity_level = request.form["activity_level"]

        bmi = weight / (height ** 2)
        if bmi < 18.5:
            health_status = "underweight"
        elif 18.5 <= bmi < 24.9:
            health_status = "normal weight"
        elif 25 <= bmi < 29.9:
            health_status = "overweight"
        else:
            health_status = "obese"

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Check if the user already has a BMI entry in the database
        existing_entry = cursor.execute(
            "SELECT * FROM user_health WHERE user_id = ?", (user_id,)
        ).fetchone()

        if existing_entry:
            # Update existing entry
            cursor.execute(
                """
                UPDATE user_health
                SET height = ?, weight = ?, age = ?, gender = ?, activity_level = ?, bmi = ?, health_status = ?
                WHERE user_id = ?
                """,
                (height, weight, age, gender, activity_level, bmi, health_status, user_id),
            )
        else:
            # Insert a new entry
            cursor.execute(
                """
                INSERT INTO user_health (user_id, height, weight, age, gender, activity_level, bmi, health_status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (user_id, height, weight, age, gender, activity_level, bmi, health_status),
            )

        conn.commit()
        conn.close()

        flash(f"Your BMI is {bmi:.2f}. You are {health_status}.", "info")

    return render_template("bmi.html")

# Logout route
@app.route('/logout')
def logout():
    session.clear()  # Clear the session
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

@app.route("/food_entry", methods=["GET", "POST"])
def food_entry():
    if "user_id" not in session:  # Ensure the user is logged in
        flash("Please log in to access this page.", "danger")
        return redirect(url_for("login"))

    if request.method == "POST":
        user_id = session["user_id"]
        day = request.form["day"]
        meal = request.form["meal"]
        foods = request.form["foods"]  # Comma-separated food items

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Save each food item in the database
        for food in foods.split(","):
            cursor.execute(
                "INSERT INTO user_food (user_id, day, meal, food) VALUES (?, ?, ?, ?)",
                (user_id, day, meal, food.strip()),
            )

        conn.commit()
        conn.close()
        flash("Food entry saved successfully!", "success")

    return render_template("food_entry.html")


if __name__ == '__main__':
    app.run(debug=True)
