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
        con = sql.connect(database)
        self.cur = con.cursor()
        self.setID = setID

    def ConfigCheck(self):
        file = open("config.txt", "r")
        config = file.readlines()[4] #reads line 4, which is where flashcard-queue is defined to be.
        config = config[20:-1] #cuts out the unecessary information, to single out the only important piece of information (true or false)
        file.close()

        #the following selection statements compare the value isolated from the file and returns a suitable boolean value.
        if config == "true": 
            self.queueFlowType = True
        elif config == "false":
            self.queueFlowType = False
        else:
            print("ERROR: CONFIGURATION FILE - WRONG FORMAT")
            quit() #since correct config format is a precondition of the subroutine, no handling is done if the data read does not go to plan. The program simply puts an error message in the console and quits.
        
        return self.queueFlowType #returns variable in classical way; may not be needed but I believe it is good to have the option to use it this way.
 
    
    def GetInput(self): #will need to be updated when packaged into a GUI.
        valid = True #used to check input is valid
        front = input("Please input front: ")
        back = input("Please input back: ")
        conf = input("Please input initial confidence: ")
        validConf = ['good', 'okay', 'bad'] #set of valid confidences, in list form for possibility of extra options in the future. 
    
        if not front: #the following statements check the inputs are not null, and if they are, change the valid variable accordingly.
            valid = False
        if not back:
            valid = False
        
        if conf not in validConf: #checks if users input is not in set of valid inputs. 
            valid = False

        if valid == False:
            print("Error")
            quit() #quits if inputs are invalid
            
        self.inputsList = [front, back, conf] #adds the three inputs into a list.

    def CardPointer(self):
        res = self.cur.execute(""" 
                                SELECT MAX(CardID)
                                FROM Flashcards
                                WHERE setID = ?;""", (self.setID,)) #executes transaction on database, to gain knowledge of current highest cardID. Use of 'res' is standard practice for SQLite package.
        cardID = res.fetchall() #fetches result of SQL transaction
        cardID = cardID[0][0]
        print(cardID)


    def FormatInputSQL(self):
        
        

class RmFlashcards: #class specifically for functions for removing flashcards.
    

    def Null():
        pass

class AddDeck: #class specifically for functions for adding a deck.
    

    def Null():
        pass

class RmDeck: #class specifically for functions for removing a deck.
    

    def Null():
        pass
