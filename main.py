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
        player = Player(self)
        self.players.append(player)
        return player

    # Blackjack Logic

    def dealerStartHand(self, dealer):
        dealer.dealCard(self.deck.available, 1)

    def dealStartHand(self, player, dealer):
        player.dealCard(self.deck.available, 2)
        self.dealerStartHand(dealer)

    def getTotal(self, player):
        hand = player.hand
        total = 0

        for i in range(len(hand)):
            total += hand[i].bJackValue
        
        return total

    def playerHit(self, player):
        card = player.dealCard(self.deck.available, 1)
        total = self.getTotal(player)
        print("New Card:", card[0].name)
        print("New Total:", total)

        if total > 21:
            print("You busted!")
        elif total == 21:
            print("21!")
        else:
            self.selectChoice(player)

    def selectChoice(self, player):
        print("Would you like to hit or stand?")
        answer = str(input("\n"))

        if answer.lower() == "hit":
            print("Hit!")
            time.sleep(1.5)
            self.playerHit(player)
        elif answer.lower() == "stand":
            print("Stand!")
        else:
            print("What?")
            time.sleep(2)
            self.selectChoice(player)

    def blackjack(self, player):
        dealer = blackJackDealer(self)
        self.deck.fullShuffle() # Shuffle + Split Deck x2
        self.dealStartHand(player, dealer)
        cls()
        player.dispHand()
        time.sleep(2)
        dealer.showDealHand()
        time.sleep(2)
        self.selectChoice(player)

class blackJackDealer():
    def __init__(self, gameObj):
        self.hand = [] # Fill with CardObjs
        self.gameObj = gameObj

    def dealCard(self, available, quant):
        am = len(available)
        for i in range(quant):
            am -= 1
            chosen = available[random.randint(1, am)]
            self.hand.append(chosen)
            available.remove(chosen)

    def showDealHand(self):
        print("Dealer is showing:")
        for card in self.hand:
            print(card.name)
        print("This amounts to:", self.gameObj.getTotal(self))

class Player():
    def __init__(self, gameObj):
        self.hand = []
        self.gameObj = gameObj

    def dealCard(self, available, quant):
        am = len(available)
        retTab = []
        for i in range(quant):
            am -= 1
            chosen = available[random.randint(1, am)]
            self.hand.append(chosen)
            retTab.append(chosen)
            available.remove(chosen)

        return retTab

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