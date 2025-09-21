import random
import os
import time
import math
import card as Card

collNums = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]   
collSuite = ["Clubs", "Spades", "Diamonds", "Hearts"]

def cls():
    os.system("cls")

class Deck():
    def __init__(self):
        self.available = []
        self.regenCards()

    def regenCards(self):
        self.available = []    
        count = 0
        cls()
        for i in range(len(collSuite)):
            for j in range(len(collNums)):
                string = Card.Card(collSuite[i], collNums[j])
                count += 1
                self.available.append(string)

                print(f"\r Added Card", str(count) + "/52", flush=True, end="")
                time.sleep(.05)

    def debugPrint(self):
        # cls()
        for i in range(len(self.available)):
            print(self.available[i].name)

    def shuffle(self):
        temp = []
        am = len(self.available)

        for i in range(am):
            ran = random.randint(0, (am - 1))
            item = self.available[ran]
            temp.append(item)
            self.available.remove(item)
            am -= 1
    
        self.available = temp

    def fullShuffle(self):
        self.shuffle()
        self.split()
        self.shuffle()
        self.split()

    def split(self):
        dAm = len(self.available)

        for i in range(dAm):
            if i > (math.floor(dAm / 2)):
                break
            else:
                self.available.append(self.available[i])
                self.available.remove(self.available[i])