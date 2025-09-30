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
    
    def __str__(self):
        return f"{self.name}"
