import sqlite3

class DatabaseRepository(object):
    _conn = None
    """Creates a singleton instance of the DatabaseRepository class.
        This ensures that only one instance of the class is created
        and shared across the application.
        The __new__ method is overridden to control the instantiation
        process. If an instance already exists, it returns that instance."""
    def __new__(cls):
            if not hasattr(cls,'instance'):
                if(cls._conn is None):
                    cls._conn = sqlite3.connect("database.db",check_same_thread=False)
                    cls._conn.row_factory = sqlite3.Row
                cls.instance = super(DatabaseRepository,cls).__new__(cls)
            return cls.instance
 
 

    @staticmethod
    def connect():
        if(DatabaseRepository._conn is None):
            DatabaseRepository._conn = sqlite3.connect("database.db")
        
    #creates the connection to the database
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
    
    #closes the connection to the database
    def close(self):
        self._conn.close()


