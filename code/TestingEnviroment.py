import FlashcardFunctions as Ff

Adder = Ff.AddFlashcards("databases/Flashcards.db", '1') #to create AddFlashcard 'Adder' object

Adder.ConfigCheck()

Ff.General.EnQueue(Adder.queue, "Test")
print(Adder.queue)

#for i in range(0,3):
#    Adder.GetInput()
#    Adder.FormatInputSQL()
#    i += 1
