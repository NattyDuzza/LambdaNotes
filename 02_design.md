# Design
## Design Sequence
The design phase of LambaNotes will be split into two main sections: designing the algorithms and backend structures, and mapping out how this will be packaged into a user interface. 

Whilst the *Analysis* section has provided a strong basis for what the program will achieve, I believe it will be advantageous to carry out the design of the two phases in the order they are given above. This is because it it possible that the design of the components will create new ideas on how to present them in a GUI. 

Furthermore, I will follow an agile development life-cycle and so work simultaneously on *Design* and *Implementation*. How I go about working on these together will be clearly stated and split over the two chapters. Whilst working on the design, if I believe it could be improve by returning to the *Analysis* stage I will do so, however any analysis added will be clearly noted with a suitable disclaimer.

## Overview
Before the design of each specific module of the program is mapped out, I believe it to be advantageous to design and analyse a zoomed-out plan for the project. This can be used to keep track of the main features of the program, and also to inform what how designs of each part of this diagram must account for communication with another (according to the arrow directions between them). 

Please see the following design:

![overview](pictures/TopDown1.drawio.png) 

These features have already been discussed however this diagram provides a clear set of possible user stories, and how each sub-feature links to others to create the overall program. 

It was a clear decision to start the flow of the program from a home screen. The user can then decide which route to go down, mind map or flashcard. ([^1]) From here, they can decide whether to make a new instance of the tool they have chosen, or to inspect/edit an instance they have already edited previously. ([^1]:Please note that, although the arrows do not directly imply it in the diagram, that a user will be able to move back to the home screen to be able to change which tool they are using.)

## Flashcards

I have decided to design this feature first since it went through less proof-of-concept prototyping in the *Analysis* phase. It is also poses a unique challenge compared to the rest of the project since it requires the combination of two programming languages (Python and SQL). 

### Overview

In this section (and elsewhere moving forward) I will refer to 'cards' and 'sets'. A 'set' is the group of flashcards, presumably holding a common topic, for example a user could create a Physics A-Level set of flashcards. 'cards' are simple a contracted way to reference flashcards.

### Flashcard Format 

The flashcards will have the following attributes:

- Front: This will include the prompt.
- Back: This will hold the answer to the prompt on the front.
- Significance: This is the attribute that will be utilised in the sorting algorithm to help decide how to order the output of flashcards.

The following shows an example set of attributes a flashcard could have:

![flashcardExample1](pictures/FlashcardExample1.drawio.png)

The significance value is placed to the side because it will not be known to the user and only be used for the backend processes. The user will, however, influence the significance through a GUI input that represents their confidence in the content of the card. These will not be attributes, since all the information about the relevance to the users learning will be stored in the significance attribute.
### Database Design

The program must be able to handle multiple sets of flashcards, with each set containing an arbritrary number of cards. 
For simplicity, if a flashcard is entered in identical form into multiple sets multiple records of the flashcard will be stored, each with a unique foreign key. There will, however, be an implementation of code to check whether there is already a record of a flashcard's Front when it is being inputted. 

The following ERD (Entity Relationship Diagram) displays how two tables will be linked through use of a foreign key so as to create the required construct for storing the flashcard information.

![flashcardERD](pictures/DatabaseDesign.drawio.png)

This design conforms to the Third Normal Form, and does not pose any problems with the relationship between the tables (e.g. not many-to-many). This provides a good basis moving forward, and will be advantageous if additions should need to be made after prototyping.


It is also important the relational database will conform to ACID rules:
- Atomicity: This will be enforced by checking the statement has been executed and, if not, diverting the flow of the program to a suitable location where the database will not be permanently affected.
- Consistency: The addition of declaritive constraints will ensure each addition conforms to the database rules.
- Isolation: Since the program will only be making transactions in a sequential manner, and the database will be stored locally with no possible outside access from other systems, Isolation will not be an issue and will be conformed to.
- Durability: To ensure that all data entered from succesful transactions is permanently stored, the database will be consistently saved at regular intervals, reducing the chance of interference from, say, a system failure. 
