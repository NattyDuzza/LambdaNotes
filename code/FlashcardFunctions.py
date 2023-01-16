class General: #class for general function that may be used my any of the proceeding classes.
    

    def Null():
        pass

class AddFlashcards: #class specifically for functions for adding flashcards.
    

    def __init__(self):
        self.queueFlowType = None

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

class RmFlashcards: #class specifically for functions for removing flashcards.
    

    def Null():
        pass

class AddDeck: #class specifically for functions for adding a deck.
    

    def Null():
        pass

class RmDeck: #class specifically for functions for removing a deck.
    

    def Null():
        pass
