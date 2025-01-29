import sqlite3

con = sqlite3.connect("test.db")

cursor = con.cursor()

#creating a table
def createTable():
    #we can specify the data type like this 
    cursor.execute("CREATE TABLE Test(test INTEGER)")
    #save the changes in the database
    con.commit()

#selecting a particular value
def select():
    res = cursor.execute("SELECT age FROM Users")
    print(res.fetchall())

#Inserting many values
def insertMany():
    data = [("sharvesh",18,20,56,56,'M'),("Siva",18,20,56,56,'M')]
    cursor.executemany("INSERT INTO Users VALUES(?,?,?,?,?,?)",data)
    con.commit()

#order by
def orderBy():
    res = cursor.execute("SELECT name,age,gender FROM Users ORDER BY phone DESC")
    print(res.fetchall())


#where
def where():
    res = cursor.execute("SELECT name,age FROM Users WHERE name='Siva'")
    print(res.fetchone())


#delete 
def delete():
   cursor.execute("DELETE FROM Users")
   con.commit()


createTable()
con.close()


