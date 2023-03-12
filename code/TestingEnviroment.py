import FlashcardFunctions as Ff

queue = Ff.General.NewQueue()

print(queue)

Ff.General.EnQueue(queue, "test1")
Ff.General.EnQueue(queue, "test2")
Ff.General.EnQueue(queue, "test3")

print(queue)