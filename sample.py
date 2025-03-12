# import sqlite3

# # Connect to SQLite database
# con = sqlite3.connect("example.db")
# cur = con.cursor()

# # Create a table (Make sure column names match dictionary keys)
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         age INTEGER,
#         city TEXT
#     )
# """)
# con.commit()

# # Python dictionary with column names as keys
# user_data = {"name": "Alice", "age": 25, "city": "New York"}

# # Dynamically generate SQL query
# columns = ", ".join(user_data.keys())  # "name, age, city"
# placeholders = ", ".join(["?"] * len(user_data))  # "?, ?, ?"

# print(columns)
# print(placeholders)


class Animal:
    def hello(self):
        pass

class Hollo:
    def hello(self):
        pass

class Lion(Animal,Hollo):
    def hello(self):
        print("hello")

lion = Lion()
lion.hello()