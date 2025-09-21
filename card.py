class Card(): # Static, doesnt do anything outside of existing + setup
    def __init__(self, suite, number):
        self.suite = suite
        self.number = number
        self.name = (number + " Of " + suite)

        try: # Getting Blackjack Value
            number = int(number)
        except ValueError:
            if number == "Ace":
                self.bJackValue = 1
            else:
                self.bJackValue = 10
        else:
            self.bJackValue = number


# class Deck():
#     def __init__(self):
#         self.available = []
#         self.regenCards()

#     def regenCards(self):
#         self.available = []    
#         for i in range(len(collSuite)):
#             for j in range(len(collNums)):
#                 string = Card.Card(collSuite[i], collNums[j])

#                 self.available.append(string)

#                 print("Added", string.name)
#                 time.sleep(.05)
#             print("<--", collSuite[i], "Complete -->")    

#     def debugPrint(self):
#         # cls()
#         for i in range(len(self.available)):
#             print(self.available[i].name)

#     def shuffle(self):
#         temp = []
#         am = len(self.available)

#         for i in range(am):
#             ran = random.randint(0, (am - 1))
#             item = self.available[ran]
#             temp.append(item)
#             self.available.remove(item)
#             am -= 1
    
#         self.available = temp
#         print("Shuffled!")

#     def fullShuffle(self):
#         self.shuffle()
#         self.split()
#         self.shuffle()
#         self.split()

#     def split(self):
#         dAm = len(self.available)

#         for i in range(dAm):
#             if i > (math.floor(dAm / 2)):
#                 break
#             else:
#                 self.available.append(self.available[i])
#                 self.available.remove(self.available[i])
#         print("Split Deck")    

# class Card(): # Static, doesnt do anything outside of existing + setup
#     def __init__(self, suite, number):
#         self.suite = suite
#         self.number = number
#         self.name = (number + " Of " + suite)