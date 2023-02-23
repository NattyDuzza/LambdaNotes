import tkinter as tk
from tkinter import ttk

class TestingWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Testing")

        self.label = tk.Label(self, text="Testing")
        self.label.pack()

class MainRemovalWin(tk.Tk):
    def __init__(self, flashcards):
        super().__init__() #initialises tk class which has been inherited
        self.multiPick = False
        self.rightFrame = tk.Frame(self)
        self.leftFrame = tk.Frame(self)

        #configuration
        self.title('LambdaNotes - Remove Flashcard')
        self.geometry('400x400')

        #frames
        self.rightFrame.grid(row=0, column=0, sticky=tk.NSEW)
        self.leftFrame.grid(row=0, column=0, sticky=tk.NSEW)

        backButton = tk.Button(self.leftFrame, text="Back", command = self.backButton)
        backButton.grid(row=0, column=0, padx=(2,2), pady=(2,10), sticky=tk.W)

        flashcardList = tk.Listbox(self.leftFrame)
        flashcardList.grid(row=1, column=0, padx=(20,0), pady=20)

        flashcardListScroll = ttk.Scrollbar(self.leftFrame, orient='vertical')
        flashcardListScroll.grid(row=1, column=1,padx=(0,20), pady=20, sticky=tk.NS)

        flashcardList.config(yscrollcommand = flashcardListScroll.set)
        flashcardListScroll.config(command = flashcardList.yview)
        
        multiPickLabel = tk.Label(self.rightFrame, text="Mutlipick:")
        multiPickLabel.grid(row=0, column=0, sticky=tk.E)

        multiPickCheck = tk.Checkbutton(self.rightFrame, variable=self.multiPick)
        multiPickCheck.grid(row=1, column=0, sticky=tk.W)



        removeFlashcardBtn = tk.Button(self, text="Remove Flashcard(s)", command= self.removeFlashcard)
        removeFlashcardBtn.grid(row=2, column=0)

#        for i in range(0, len(flashcards)):
 #           flashcardList.insert(tk.END, flashcards[i])
        for i in range(0, 1000):
            flashcardList.insert(tk.END, i)

    def backButton(self):
       pass

    def removeFlashcard(self):
        pass

  

MainRemovalWin([1, 2, 3, 4, 5]).mainloop()