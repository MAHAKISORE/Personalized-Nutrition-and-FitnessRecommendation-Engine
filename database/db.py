import sqlite3

class DataBase:
    def __init__(self):
        connection = sqlite3.connect("database.db")
        self._conn = connection

    def createTables(self):
        try:
            cursor = self._conn.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS Name (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
            age INT,
            phone INTEGER,
            height INTEGER,
            weight INTEGER,
            gender TEXT
            );
                """)
            
            self._conn.commit() 
        except sqlite3.Error as e:
            print(e)
    

    
    def close(self):
        self._conn.close()

