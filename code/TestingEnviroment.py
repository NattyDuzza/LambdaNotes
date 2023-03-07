import FlashcardFunctions as Ff

Adder = Ff.AddFlashcards("databases/Flashcards.db", '3') #to create AddFlashcard 'Adder' object

Adder.ConfigCheck()

for i in range(0,3):
  Adder.GetInput()
  Adder.FormatInputSQL()
  i += 1
