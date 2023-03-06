import FlashcardFunctions as Ff
import sqlite3 as sql

#database connection
database = "databases/Flashcards.db"

#subroutines
def FlashcardList(setID):

    con = sql.connect(database)
    cur = con.cursor()

    li = []
    
    adder = Ff.AddFlashcards(database, setID)
    maxID = adder.CardPointer()

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

def RemoveFlashcards(setID, rmList):
    remover = Ff.RmFlashcards(database, setID)
    remover.Remove(rmList)