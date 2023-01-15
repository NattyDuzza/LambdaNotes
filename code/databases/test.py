import sqlite3 as sql #imports package into Python under more efficient name

con = sql.connect("test.db") #creates a connection to the database test.db.
# test.db will be created in the current working directory if not already made.

cur = con.cursor() #creates a database cursor which is needed to execute statements and retrieve data.

cur.execute("""CREATE TABLE movie(
            title varchar primary key,
            year int,
            score float
            )""") #uses the cursor to execute the SQL on the database currently connected.

cur.execute("INSERT INTO movie(title, year, score) VALUES ('test', 2022, 10.0)")

con.commit() #commits the transactions

