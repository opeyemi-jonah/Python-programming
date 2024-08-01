import sqlite3 as sql

conn = sql.connect("SampleDB.db")
curs = conn.cursor() #crud commands 
curs.execute("Create table Customer(name varchar(50), contact varchar(25))")

conn.commit()

conn.close()