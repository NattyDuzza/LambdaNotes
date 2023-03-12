# Testing Plan

## Testing During Initial Implementation

As I write the code to implement the design, I will continually test its functionality to judge whether I am ready to move on to the next section to implement. 

The following sections list what is needed of each section that I implement for it to be able to be classed as complete:

### User Adds Flashcard

#### ConfigCheck

##### Iteration 1

- Successfully reads from designated text file
- Successfully isolates needed information from text file
- Successfully updates variable depending on information
- Can handle erroneous inputs

##### Iteration 2 - Added Tests

- Successfully creates queue if needed

#### GetInput

##### Iteration 1

- Can check if confidence inputs are valid and feedback if not
- Can check if input fields are Null / empty

##### Iteration 2 - Added Tests

- Can work in tandem with whole UI (tested through full application tests)

#### CardPointer

##### Iteration 1

- Can return the max cardID in a cardset in an optimal format
- Can account for removal of card with the current max cardID

##### Iteration 2 - Added Tests

- Default cardID is set to 0

##### Iteration 3 - Added Tests

- Can return the max cardID in the *whole database* (tested through integration with other tested modules)

#### NewQueue + EnQueue

- Can create a list and append successfully

#### FormatInputSQL

- Can succesfully add a flashcard to the persistent database.
- Can handle different flow types / expandable to having queue offloading input

