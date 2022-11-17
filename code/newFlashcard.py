import random

flashcards = []

class Flashcard:

    def __init__(self, confidence):
        self.confidence = confidence
        self.significance = 10 # Current starting significance, will be updated depending on how testing goes.

    def update(self):
        self.confidence = input('Confidence: ')
        if self.confidence == 'good':
            self.significance -= (3 + round(random.uniform(-0.9,2.1), 3)) # Random element to it so that the flashcards do not all have the same significance.
        if self.confidence == 'bad':
            self.significance += (3 + round(random.uniform(0.9, 3.1), 3))
  
  # The following lines are here to reproduce a readable indicator of which instance of the class we are looking at whilst prototyping.
    def __repr__(self):
        return f"{self.significance}"

    def __str__(self):
        return f"{self.significance}"


def sort(data): #Bubble sort method, will aim to update to quicker sort incase of larger flashcards decks. Sorted on significance.
    for i in range(0, len(data) -2):
        for j in range(0, len(data) - i - 1):
            if data[j].significance > data[j+1].significance:
                data[j], data[j+1] = data[j+1], data[j]

    print(data)
    


for i in range(0, 10): # Prototyping function to create flashcards, no additional data other than confidence added so as to make prototyping more efficient.
    confidence = input('input: ')
    flashcards.append(Flashcard(confidence))

for j in range(0, len(flashcards)):
    #print(flashcards[j].confidence)
    flashcards[j].update()
    print(flashcards[j].significance)
sort(flashcards)

    
