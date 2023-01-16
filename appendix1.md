# Appendix

## States of TestingEnvironment.py
During development I have used a python script called *TestingEnvironment.py* extensively to test the code as it has been added to. In many places I have included the test code in full, however when only a small edit to the testing code is made I have usually simply described the edit I made. For clarity, I have included each iteration like this here. The reference system (e.g. [1.1]) is used throughout the project to refer to here.

##### [1.1] 

```python
import FlashcardFunctions as Ff

print(Ff.AddFlashcards.ConfigCheck())
```

##### [1.2]

```python
import FlashcardFunctions as Ff

Adder = Ff.AddFlashcards()

print(Adder.ConfigCheck())
```
