import sqlite3

con = sqlite3.connect("test.db")

cursor = con.cursor()

#cursor.execute("CREATE TABLE Users(name,age,phone,height,weight,gender)")
cursor.execute(" INSERT INTO Users VALUES('Sharvesh',12,34,34,45,'M') ")
con.commit()