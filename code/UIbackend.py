import FlashcardFunctions as Ff
import sqlite3 as sql

#database connection
database = "databases/Flashcards.db"

#to create object to track variables that will be needed in different UI windows
class Tracker:
    def __init__(self, setID):
        self.setID = setID

#subroutines
def FlashcardList(setID):

    con = sql.connect(database)
    cur = con.cursor()

    li = []
    
    adder = Ff.AddFlashcards(database, setID)
    maxID = adder.SetCardPointer()

    for i in range(0, maxID+1):
        try:
            res = cur.execute("""
                                SELECT front
                                FROM Flashcards
                                WHERE setID = ? AND
                                cardID = ?;""", (setID, i))
            flashcard = res.fetchall()

            
            if len(flashcard) == 0:
                pass
            else:
                flashcard = {flashcard[0][0]:i}
                li.append(flashcard)

        except sql.Error:
            print("Error")

    return li

def CardsetList():

    con = sql.connect(database)
    cur = con.cursor()

    li = []

    res = cur.execute("""SELECT * FROM Cardset;""")

    res = res.fetchall()
    
    for i in range(0, len(res)):
        li.append(res[i][1])
    
    return li

def changeSetID(setName):
    con = sql.connect(database)
    cur = con.cursor()

    res = cur.execute("""SELECT setID FROM Cardset
    WHERE setName=?;""",(setName,))

    res = res.fetchall()[0][0]
    return res
    
def RemoveFlashcards(setID, rmList):
    remover = Ff.RmFlashcards(database, setID)
    remover.Remove(rmList)