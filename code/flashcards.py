import random

x = 0
flashcardsGood = []
flashcardsOkay= []
flashcardsBad = []

class Flashcard():
    def __init__(self):
        self.front = input("Front: ")
        self.back = input("Back: ")
        self.confidence = input("Confidence: ")

    def update_confidence(self):
        confidenceNew = input("Confidence: ")
        if confidenceNew != self.confidence:
            self.confidence = confidenceNew
            return 1
    
def flashcard_run(good, okay, bad):
    if len(bad) != 0:
        for i in range(0, len(bad)):
            print(bad[i].front)
            input("Press Enter to see back") 
            print(bad[i].back)
            if bad[i].update_confidence() == 1:
                flashcard_sort(bad[i])
        return False


def flashcard_sort(flash):
    if flash.confidence == 'Good':
        flashcardsGood.append(flash)
    elif flash.confidence == 'Okay':
        flashcardsOkay.append(flash)
    elif flash.confidence == 'Bad':
        flashcardsBad.append(flash)
    else:
        print("Not configured confidence level")
    

while x<3:
    flash = Flashcard()
    flashcard_sort(flash)
    x+=1

while True:
    if flashcard_run(flashcardsGood, flashcardsOkay, flashcardsBad):
        pass
    break

# for i in range(0, len(flashcardsGood)):
   # print(flashcardsGood[i].front, flashcardsOkay[i].front, flashcardsBad[i].front)

