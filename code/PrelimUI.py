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

        #configuration
        self.title('LambdaNotes - Remove Flashcard')
        self.geometry('400x400')

        flashcardList = tk.Listbox(self)
        flashcardList.grid(row=0, column=0)

        flashcardListScroll = ttk.Scrollbar(self, orient='vertical')
        flashcardListScroll.grid(row=0, column=1, sticky=tk.NS)

        flashcardList.config(yscrollcommand = flashcardListScroll.set)
        flashcardListScroll.config(command = flashcardList.yview)
        
#        for i in range(0, len(flashcards)):
 #           flashcardList.insert(tk.END, flashcards[i])
        for i in range(0, 1000):
            flashcardList.insert(tk.END, i)
        
MainRemovalWin([1, 2, 3, 4, 5]).mainloop()
