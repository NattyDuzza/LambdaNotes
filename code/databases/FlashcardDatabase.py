import sqlite3 as sql #imports package into Python under more efficient name

con = sql.connect("Flashcards.db") #creates a connection to the database test.db.
# Flashcards.db will be created in the current working directory if not already made.

cur = con.cursor() #creates a database cursor which is needed to execute statements and retrieve data.

cur.execute("""
            CREATE TABLE Cardset(
            setID int primary key NOT NULL,
            setName varchar NOT null
            );""")

cur.execute("""            
            CREATE TABLE Flashcards(
            cardID int primary key NOT NULL,
            front varchar NOT NULL,
            back varchar NOT NULL,
            significance float NOT NULL,
            setID int NOT NULL,
            CONSTRAINT FK_setID foreign key (setID)
            REFERENCES Cardset(setID)
            );
            """) #creates tables

cur.execute("""
            INSERT INTO Cardset(setID, setName) VALUES (001, "Computer Science");
            """)

cur.execute("""
            INSERT INTO FLashcards
            (cardID, front, back, significance, setID) VALUES (001, "a", "b", 10.0, 001);
            """)

con.commit() #commits the transactions

