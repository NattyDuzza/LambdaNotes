import FlashcardFunctions as Ff
import sqlite3 as sql

#database connection
database = "databases/Flashcards.db"
con = sql.connect(database)
cur = con.cursor()

#subroutines
def FlashcardList(setID):
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
                li.append(flashcard[0][0])

        except sql.Error:
            print("Error")

    return li
