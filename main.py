import random
import os
import time
import card as Card
import deck as Deck

collNums = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]   
collSuite = ["Clubs", "Spades", "Diamonds", "Hearts"]

def cls():
    os.system("cls")

class Game():
    def __init__(self, gamemode):
        self.gamemode = gamemode
        self.players = []
        self.deck = Deck.Deck()

        if gamemode == "blackjack":
            playerObj = self.addPlayer()
            self.blackjack(playerObj)
    
    def dealPlayers(self):
        for player in self.players:
            player.dealSingular(self.deck.available)

    def addPlayer(self):
        player = Player()
        self.players.append(player, self)
        return player

    # Blackjack Logic

    def dealStartHand(self, player):
        player.dealCard(self.deck.available, 2)

    def getTotal(self, player):
        hand = player.hand
        total = 0

        for i in range(len(hand)):
            total += hand[i].bJackValue
        
        return total

    def blackjack(self, player):
        self.deck.fullShuffle() # Shuffle + Split Deck x2
        self.dealStartHand(player)
        cls()
        player.dispHand()

class blackJackDealer():
    def __init__(self, hand, gameObj):
        self.hand = [] # Fill with CardObjs
        self.gameObj = gameObj

    def dealCard(self, available, quant):
        am = len(available)
        for i in range(quant):
            am -= 1
            chosen = available[random.randint(1, am)]
            self.hand.append(chosen)
            available.remove(chosen)

class Player():
    def __init__(self, gameObj):
        self.hand = []
        self.gameObj = gameObj

    def dealCard(self, available, quant):
        am = len(available)
        for i in range(quant):
            am -= 1
            chosen = available[random.randint(1, am)]
            self.hand.append(chosen)
            available.remove(chosen)

    def dispHand(self):
        print("Your hand is:")
        for card in self.hand:
            print(card.name)
        print("This amounts to:", self.gameObj.getTotal(self))

def mainLoop():
    print("Welcome to thomedome's Card Games!")
    time.sleep(1.5)
    cls()
    gameChoice = str(input("What would you like to play? \n"))
    corrected = gameChoice.lower()

    game = Game(gamemode=corrected)

mainLoop()