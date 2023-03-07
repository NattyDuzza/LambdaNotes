import tkinter as tk
from tkinter import ttk
import UIbackend as UI

database = "databases/Flashcards.db"

class TestingWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Testing")

        self.label = tk.Label(self, text="Testing")
        self.label.pack()

class MainRemovalWin(tk.Tk):
    def __init__(self):
        super().__init__() #initialises tk class which has been inherited
        self.multiPick = tk.IntVar(self)

        #window configuration
        self.title('LambdaNotes - Remove Flashcard')
        self.geometry('400x400')

        #----------------------------------------------------

        #frames
        self.topBarFrame = tk.Frame(self)
        self.rightFrame = tk.Frame(self)
        self.leftFrame = tk.Frame(self)
        self.multiPickFrame = tk.Frame(self.rightFrame)

        self.topBarFrame.grid(row=0, column=0, sticky=tk.NSEW)
        self.rightFrame.grid(row=1, column=1, sticky=tk.NSEW)
        self.leftFrame.grid(row=1, column=0, sticky=tk.NSEW)
        self.multiPickFrame.grid(row=0, column=0, sticky=tk.NSEW)

        #-------------------------------------------------------------------------------------
        
        #elements

        backButton = tk.Button(self.topBarFrame, text="Back", command = self.backButton)
        backButton.grid(row=0, column=0, padx=(2,2), pady=(2,10), sticky=tk.W)

        self.flashcardList = tk.Listbox(self.leftFrame, selectmode=tk.SINGLE)
        self.flashcardList.grid(row=1, column=0, padx=(20,0), pady=20)

        flashcardListScroll = ttk.Scrollbar(self.leftFrame, orient='vertical')
        flashcardListScroll.grid(row=1, column=1,padx=(0,20), pady=20, sticky=tk.NS)

        self.flashcardList.config(yscrollcommand = flashcardListScroll.set)
        flashcardListScroll.config(command = self.flashcardList.yview)
        
        multiPickLabel = tk.Label(self.multiPickFrame, text="Mutlipick:")
        multiPickLabel.grid(row=0, column=0, pady=(20, 5), sticky=tk.E)

        self.multiPickCheck = tk.Checkbutton(self.multiPickFrame, variable=self.multiPick, command=self.multiPickCheck)
        self.multiPickCheck.grid(row=0, column=1, pady=(20, 5), sticky=tk.W)

        removeFlashcardBtn = tk.Button(self.rightFrame, text="Remove Flashcard(s)", command=self.removeFlashcard)
        removeFlashcardBtn.grid(row=2, column=0, pady=(7,0))

        changeCardsetBtn = tk.Button(self.rightFrame, text="Charge Cardset", command=self.changeCardset)
        changeCardsetBtn.grid(row=3, column=0, pady=(7,0))

        #------------------------------------------------------------------------------------------------------------------

        #prelim subroutines
        self.updateList()

    def updateList(self):   
        self.flashcardList.delete(0, tk.END)
        self.scrollListContent = UI.FlashcardList(track.setID)
        for i in range(0, len(self.scrollListContent)):
            self.flashcardList.insert(tk.END, self.scrollListContent[i])

    def backButton(self):
       pass

    def removeFlashcard(self):
        rmList = []
        selectedCards = self.flashcardList.curselection()
        for i in range(0, len(selectedCards)):
            print(self.scrollListContent[selectedCards[i]])
            ID = list(self.scrollListContent[selectedCards[i]].values())[0]
            rmList.append(ID)
        UI.RemoveFlashcards(track.setID, rmList)
        print("check")
        self.updateList()

    def changeCardset(self):
        self.destroy()
        ChangeCardset().mainloop()

    def multiPickCheck(self):    #function determines whether the user has decided to choose multiple flashcards at once and changes the select mode accordingly.
        if self.multiPick.get() == 0:
            self.flashcardList.config(selectmode=tk.SINGLE)
            print(self.multiPick)
        if self.multiPick.get() == 1:
            self.flashcardList.config(selectmode=tk.MULTIPLE)
            print(self.multiPick)


class ChangeCardset(tk.Tk):
    def __init__(self):
        super().__init__()

        #window configuration
        self.title("LamdaNotes - Change Cardset")

        #----------------------------------------------

        #frames
        self.midframe = tk.Frame(self)

        self.midframe.grid(row=1, column=0)

        #elements

        introLabel = tk.Label(self, text="Choose Cardset:")
        introLabel.grid(row = 0, column=0)

        self.cardsetList = tk.Listbox(self.midframe, selectmode=tk.SINGLE)
        self.cardsetList.grid(row=0, column=0, padx=(20,0), pady=20)

        cardsetListScroll = ttk.Scrollbar(self.midframe, orient='vertical')
        cardsetListScroll.grid(row=0, column=1,padx=(0,20), pady=20, sticky=tk.NS)

        self.cardsetList.config(yscrollcommand = cardsetListScroll.set)
        cardsetListScroll.config(command = self.cardsetList.yview)

        chooseBtn = tk.Button(self, text="Confirm", command=self.confirmChange)
        chooseBtn.grid(row = 2, column=0, sticky=tk.EW)

        self.updateList()

    def updateList(self):
        self.content = UI.CardsetList()
        for i in range(0, len(self.content)):
            self.cardsetList.insert(tk.END, self.content[i])
    
    def confirmChange(self):
        selectedSet = self.content[self.cardsetList.curselection()[0]]
        track.setID = UI.changeSetID(selectedSet)
        self.destroy()
        #frames
        self.midframe = tk.Frame(self)

        self.midframe.grid(row=1, column=0)

        #elements

        introLabel = tk.Label(self, text="Choose Cardset:")
        introLabel.grid(row = 0, column=0)

        self.cardsetList = tk.Listbox(self.midframe, selectmode=tk.SINGLE)
        self.cardsetList.grid(row=0, column=0, padx=(20,0), pady=20)

        cardsetListScroll = ttk.Scrollbar(self.midframe, orient='vertical')
        cardsetListScroll.grid(row=0, column=1,padx=(0,20), pady=20, sticky=tk.NS)

        self.cardsetList.config(yscrollcommand = cardsetListScroll.set)
        cardsetListScroll.config(command = self.cardsetList.yview)

        chooseBtn = tk.Button(self, text="Confirm", command=self.confirmChange)
        chooseBtn.grid(row = 2, column=0, sticky=tk.EW)

        self.updateList()

    def updateList(self):
        self.content = UI.CardsetList()
        for i in range(0, len(self.content)):
            self.cardsetList.insert(tk.END, self.content[i])
    
    def confirmChange(self):
        selectedSet = self.content[self.cardsetList.curselection()[0]]
        track.setID = UI.changeSetID(selectedSet)
        self.destroy()
        MainRemovalWin().mainloop()
        
class AddFlashcard(tk.Tk):
    
    def __init__(self):
        super().__init__()
        UI.MakeAdderObject(track.setID)

        self.front = tk.StringVar(self)
        self.back = tk.StringVar(self)


        #window configuration
        self.title("LamdaNotes - Add Flashcard")
        self.geometry('750x550')

        #--------------------------------------------
        
        #frames

        self.topBarFrame = tk.Frame(self)
        self.FlashcardFrontEntryFrame = tk.Frame(self)
        self.FlashcardBackEntryFrame = tk.Frame(self)
        self.confBtnFrame = tk.Frame(self)
        self.confBtnSubframe = tk.Frame(self.confBtnFrame)
        self.bottomBarFrame = tk.Frame(self)

        self.topBarFrame.grid(row=0, column=0, sticky=tk.W, padx=15, pady=15)
        self.FlashcardFrontEntryFrame.grid(row=2, column=0, sticky=tk.NSEW, padx=15, pady=15)
        self.FlashcardBackEntryFrame.grid(row=3, column=0, sticky=tk.NSEW, padx=15, pady=15)
        self.confBtnFrame.grid(row=4, column=0, sticky=tk.NSEW, padx=15, pady=(15,30))
        self.confBtnSubframe.place(relx=0.1, rely=0.1, anchor=tk.CENTER)
        self.bottomBarFrame.grid(row=5, column=0, sticky=tk.E, padx=15, pady=15)
        #---------------------------------------------------------------------------------------

        #elements

        backButton = tk.Button(self.topBarFrame, text="Back", command = self.backButton)
        backButton.grid(row=0, column=0, padx=(2,2), pady=(2,10), sticky=tk.W)

        FlashcardFrontLbl = tk.Label(self.FlashcardFrontEntryFrame, text="Flashcard Front:", font=('Arial', 17))
        FlashcardFrontLbl.grid(row=0, column=0, sticky=tk.EW)

        self.FlashcardFrontEntry = tk.Entry(self.FlashcardFrontEntryFrame, width=100, textvariable=self.front)
        self.FlashcardFrontEntry.grid(row=1, column=0, sticky=tk.NSEW, ipady=30)

        FlashcardBackLbl = tk.Label(self.FlashcardBackEntryFrame, text="Flashcard Back: ", font=('Arial', 17))
        FlashcardBackLbl.grid(row=0, column=0, sticky=tk.EW)

        self.FlashcardBackEntry = tk.Entry(self.FlashcardBackEntryFrame, width=100, textvariable=self.back)
        self.FlashcardBackEntry.grid(row=1, column=0, sticky=tk.NSEW, ipady=30)

        self.confGoodBtn = tk.Button(self.confBtnSubframe, text="Good", command = lambda: self.confButton('good'))
        self.confGoodBtn.grid(row=0, column=0, sticky=tk.NSEW, padx=15, pady=15)

        self.confOkayBtn = tk.Button(self.confBtnSubframe, text="Okay", command = lambda: self.confButton('okay'))
        self.confOkayBtn.grid(row=0, column=1, sticky=tk.NSEW, padx=15, pady=15)

        self.confBadBtn = tk.Button(self.confBtnSubframe, text="Bad", command = lambda: self.confButton('bad'))
        self.confBadBtn.grid(row=0, column=2, sticky=tk.NSEW, padx=15, pady=15)

        self.condfirmButton = tk.Button(self.bottomBarFrame, text="Confirm and Add Flashcard", command=lambda: self.confirmAdd)
        self.condfirmButton.grid(row=0, column=0, sticky=tk.E, padx=15, pady=15)

    def confButton(self, conf):
        self.confidence = conf
        print(self.confidence)

    def backButton(self):
        pass

    def confirmAdd(self):
        pass

    


track = UI.Tracker(1)
#MainRemovalWin().mainloop()
AddFlashcard().mainloop()
