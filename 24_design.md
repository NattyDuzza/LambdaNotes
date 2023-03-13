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

### Preliminary UI

The following tests will be spread around the implementation, since the preliminary UI will be used to front end all major functions. They may not be pointed out at each point specifically, however it will be clear to see them being satisfied as I itertively test and implement PrelimUI.

- Can show that Tkinter is successfully being utilised by the system
- Can work with the already created backend code in FlashcardFunctions (small edits will be needed to backend code)
- Has a window for each of the following:
  - Menu
  - Creating Mindmap
  - Revising Flashcards
  - Adding Flashcards
  - Removing Flashcards
- Create a working back button function that can be used in any window where it is needed.

### Mind Map Creation

- Can successfully recreate a given mindmap using my implementation
- Successfully handles and notifies users of errors

## Evaluative Testing

After I finish the implementation of the scope of the project, I will do full build tests. These will be split into the following sections:

- Function Testing: Testing the functionality using multiple input datums in the different modules. Aims to build upon the more basic iterative testing during development.

- User Simulation Testing: I will design tests to simulate what would happen if different kind of users attempted to use LambdaNotes

- Stakeholder Testing: I will ship the final implementation to my stakeholders for them to test and gain feedback from

Between each stage, I will perform maintance on the code to fix any major bugs that were found.

### Function Testing

#### Adding Flashcards

I will test the following:

- Valid Testing: I will try to put very long front and backs into the addition window and see how it responds
- Erroneous Testing: 
  - I will try to add a card with empty front and backs

  - I will try to add a card without setting a confidence

- SQL Injection: Since the values in the entry fields are being input into an SQL database, I will perform a simple test that I cannot break the integrity of the database by inputting an SQL statement.

#### Revising Flashcards

I will test the following:

- Valid Testing: I will try using the revision window when there is only 1, 2 and 3 cards in the chosen cardset.

- Erroneous Testing: I will try opening the revision window using an empty cardset.

#### Removing Flashcards

I will test the following:

- Erroneous Testing: I will see how the program reacts when I click to remove a flashcard when:
  
  - The chosen cardset is populated and I have no card selected.
  
  - The chosen cardset is empty.

#### Mind Map Creation

I will test the following:

- Valid Testing: 
  - I will attempt to create a mind map with only one node.

  - I will attempt to create a mindmap with approx. 20 elements.

- Erronenous Testing:
  - I will see how the program reacts when I click to create a mindmap when no nodes have been added.

### User Simulation Testing

#### Technologically Adept Student

This test will simulate an experienced student making use of the software. They will spend a significant time creating flashcards on the subject of Computer Science, before using the Revise Flashcard feature to try and learn 20 of the set they create. 

Once finished, to help them remember a specific topic which was of particular struggle to remember, they will create a mind map centred around that topic. 

They will retrieve the mind map output file and exit the program. 

##### What Does This Test Look For?

- Whether the program is suitable for students
- Whether the program can cope with extensive use
- Whether the program can genuinely help someone revise and improve their knowledge of a particular topic
- Whether any usability issues become clear after extended use

#### Business Management

This test will simulate a buisness-person using the mind map feature to plan out ideas for a company conference.

They will use 



