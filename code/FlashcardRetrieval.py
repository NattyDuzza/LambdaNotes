import random
import sqlite3 as sql

database = 'databases/Flashcards.db'

class Retriever:
    
    def __init__(self, setID, window):
        self.window = window
        self.setID = setID
        self.setSize = 20
        self.con = sql.connect(database)
        self.cur = self.con.cursor()
        self.i = 0
        self.initialSort = False
    
    def main(self):
        res = self.cur.execute("""SELECT cardID FROM Flashcards
                                  WHERE setID = ?;""", (self.setID,))
        list1 = list(res.fetchall())

        self.endList = []

        for i in range(0, self.setSize):
            if len(list1) == 0:
                break
            randIndex = random.randint(0, len(list1)-1)
            element = list1[randIndex][0]
            elementSignificance = (self.cur.execute("""SELECT significance FROM Flashcards
                                                     WHERE cardID = ?""", (element,))).fetchall()[0][0]
            self.endList.append([elementSignificance, element])
            list1.pop(randIndex)

    def sort(self, list):
        for Pass in range(0, len(list)-2):
            for i in range(0, len(list)-1-Pass):
                if list[i][0] > list[i+1][0]:
                    temp = list[i]
                    list[i] = list[i+1]
                    list[i+1] = temp
        return list
    
    def retrieveFront(self):
        self.i += 1

        if self.initialSort == False:
            self.endList = self.sort(self.endList)
            self.initialSort = True
        if self.i > 2:
            self.endList = self.sort(self.endList)
            self.i=0
        
        self.id = self.endList[self.i][1]
        print(self.id)
        front = self.cur.execute("SELECT front FROM Flashcards WHERE cardID=?",(self.id,)).fetchall()[0][0]
        self.window.frontLabel.config(text = front)

    def retrieveBack(self):
        back = self.cur.execute("SELECT back FROM Flashcards WHERE cardID=?",(self.id,)).fetchall()[0][0]
        self.window.backLabel.config(text = back)

    def setConfidence(self):
        confidence = self.window.confidence

        randomAddition = random.uniform(-0.5, 0.5)
        
        if confidence == 'good':
            if (self.endList[self.i][0] + (3+ randomAddition) )< 0:
                self.endList[self.i][0] = 0
            else:
                self.endList[self.i][0] += (3 + randomAddition)
            self.cur.execute("""UPDATE Flashcards
                                SET significance=?
                                WHERE cardID=?""",(self.endList[self.i][0], self.id))
            self.con.commit()

        if confidence == 'okay':
            if (self.endList[self.i][0] + randomAddition) < 0:
                self.endList[self.i][0] = 0
            else:
                self.endList[self.i][0] += (0 + randomAddition)
            self.cur.execute("""UPDATE Flashcards
                                SET significance=?
                                WHERE cardID=?""",(self.endList[self.i][0], self.id))
            self.con.commit()

        if confidence == 'bad':
            if (self.endList[self.i][0] + (-3 + randomAddition)) < 0:
                self.endList[self.i][0] = 0
            else:
                self.endList[self.i][0] += (-3 + randomAddition)
            self.cur.execute("""UPDATE Flashcards
                                SET significance=?
                                WHERE cardID=?""",(self.endList[self.i][0], self.id))
            self.con.commit()

        #print(self.endList)#prototyping
        self.con = sql.connect(database)
        self.cur = self.con.cursor() #reconnect to database to notice previous changes


#new = Retriever(1)#prototyping
#new.main()#prototyping

#while True:
    #new.retrieve()