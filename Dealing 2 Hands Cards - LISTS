"""
Write a program that deals two “hands” of five random playing cards. Repeats not allowed.
"""
import random

types = ["Clubs", "Diamonds", "Hearts", "Spades"]
numbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
deck = []
newDeck1 = []
newDeck2 = []
count = 0

for i in types:
  for j in numbers:
    deck.append(i + " of " + j)
    
random.shuffle(deck)

for i in range(5):
  newDeck1.append(deck[count])
  newDeck2.append(deck[count + 1])
  count += 1

print(newDeck1)
print(newDeck2)
