from random import *

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

deck = []

for s in suits:
    for v in values:
        deck.append(v + " of " + s)
        
shuffle(deck)
hand = deck[:5]
print (hand)
