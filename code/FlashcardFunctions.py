import sqlite3 as sql
class General: #class for general function that may be used my any of the proceeding classes.

    def NewQueue(): #creates list to act as queue.
        queue = []
        return queue

    def EnQueue(queue, element): #takes in a pointer to a list and the element to be added, and appends the element to the list.
        queue.append(element)

class AddFlashcards: #class specifically for functions for adding flashcards.
    

    def __init__(self, database, setID):
        self.queueFlowType = None
        self.con = sql.connect(database)
        self.cur = self.con.cursor()
        self.setID = setID

    def ConfigCheck(self):
        file = open("config.txt", "r")
        config = file.readlines()[4] #reads line 4, which is where flashcard-queue is defined to be.
        config = config[20:-1] #cuts out the unecessary information, to single out the only important piece of information (true or false)
        file.close()

        #the following selection statements compare the value isolated from the file and returns a suitable boolean value.
        if config == "true": 
            self.queueFlowType = True
            self.queue = General.NewQueue()
        elif config == "false":
            self.queueFlowType = False
        else:
            print("ERROR: CONFIGURATION FILE - WRONG FORMAT")
            quit() #since correct config format is a precondition of the subroutine, no handling is done if the data read does not go to plan. The program simply puts an error message in the console and quits.
        
        return self.queueFlowType #returns variable in classical way; may not be needed but I believe it is good to have the option to use it this way.
 
    
    def GetInput(self, inpFront, inpBack, inpConf): #will need to be updated when packaged into a GUI.
        valid = True #used to check input is valid
        front = inpFront
        back = inpBack
        conf = inpConf
        validConf = ['good', 'okay', 'bad'] #set of valid confidences, in list form for possibility of extra options in the future. 
    
        if not front: #the following statements check the inputs are not null, and if they are, change the valid variable accordingly.
            print("front")
            valid = False
        if not back:
            print("back")
            valid = False
        
        if conf not in validConf: #checks if users input is not in set of valid inputs. 
            print("conf")
            valid = False

        if valid == False:
            print("Error")
            quit() #quits if inputs are invalid
            
        self.inputsList = [front, back, conf] #adds the three inputs into a list.

    def SetCardPointer(self):

        res = self.cur.execute(""" 
                                SELECT MAX(CardID)
                                FROM Flashcards
                                WHERE setID = ?;""", (self.setID,)) #executes transaction on database, to gain knowledge of current highest cardID in a specific cardset. Use of 'res' is standard practice for SQLite package.
        cardID = res.fetchall() #fetches result of SQL transaction
        cardID = cardID[0][0]
        
        if cardID is None:
            cardID = 0

        return cardID

    def CardPointer(self):
        
        res = self.cur.execute(""" 
                                SELECT MAX(CardID)
                                FROM Flashcards;""") #executes transaction on database, to gain knowledge of current highest cardID. Use of 'res' is standard practice for SQLite package.
        cardID = res.fetchall() #fetches result of SQL transaction
        cardID = cardID[0][0]
        
        if cardID is None:
            cardID = 0

        return cardID

    def FormatInputSQL(self, front=None, back=None):
        if front == None:      #This set of statements is to use the obejct variables if required.
            front = self.inputsList[0] #It is unlikely one would be None and the other not, but I still include the check for robustness.
        if back == None:
            back = self.inputsList[1]

        self.cur.execute("""
                    INSERT INTO Flashcards(cardID, front, back, significance, setID)
                    VALUES (?, ?, ?, 10, ?);""", (self.CardPointer()+1, front, back, self.setID))
        
        if self.queueFlowType == False:
            self.con.commit()

class RmFlashcards: #class specifically for functions for removing flashcards.
    
    def __init__(self, database, setID):
        self.con = sql.connect(database)
        self.cur = self.con.cursor()
        self.setID = setID

    def Remove(self, rmList):
        print("called")
        
        for i in range(0, len(rmList)):
            print(rmList[i])
            self.cur.execute(
                """
                DELETE FROM Flashcards
                WHERE setID=? AND cardID=?;
                """, (self.setID, rmList[i])
            )
            self.con.commit()


class AddDeck: #class specifically for functions for adding a deck.
    

    def Null():
        pass

class RmDeck: #class specifically for functions for removing a deck.
    

    def Null():
        pass
