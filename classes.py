
card_A = {'Ad':('A dice', 50),'Af':('A flower', 50),'As':('A spade', 50),'Ah':('A heart', 50)}

class Card:
    def __init__(self):
        self.cardSuit = ['Dice', 'Spade', 'Flower', 'Heart']

    def printc(self):
        for i in self.cardSuit:
            print(i)
        
Card.printc(self)
