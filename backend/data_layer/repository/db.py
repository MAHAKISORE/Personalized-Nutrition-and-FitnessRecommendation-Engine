import sqlite3
from threading import Lock

class DataBase(object):
    _conn = None
    _lock = Lock()
    def __new__(cls):
        with cls._lock:
            if not hasattr(cls,'instance'):
                if(cls._conn is None):
                    cls._conn = sqlite3.connect("database.db",check_same_thread=False)
                    cls._conn.row_factory = sqlite3.Row
                cls.instance = super(DataBase,cls).__new__(cls)
            return cls.instance
 
    # def __init__(self):
    #     connection = sqlite3.connect("database.db")
    #     connection.row_factory = sqlite3.Row
    #     self._conn = connection
    def createTables(self):
        try:
            cursor = self._conn.cursor()
            cursor.execute(""" CREATE TABLE Users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
            age INT,
            email TEXT,
            height INTEGER,
            weight INTEGER,
            gender TEXT,
            pwd TEXT
            );
                """)
            
            self._conn.commit() 
        except sqlite3.Error as e:
            print(e)
    
    def deleteTable(self):
        self._conn.execute("DROP TABLE Users")
    
    def close(self):
        self._conn.close()


