import random

cardNum = []
hand1 = []
hand2 = []
win1 = 0
win2 = 0

amount = random.randrange(10,100,2)

for num in range(amount + 1):
  cardNum.append(num)

print(cardNum) #Level 2
print()
random.shuffle(cardNum)

for place in range(0,len(cardNum)-1,2):
  hand1.append(cardNum[place])
  hand2.append(cardNum[place+1])

print(hand1,hand2) #Level 3
print()

for round in range(len(hand1)):
  if hand1[round] > hand2[round]:
    winner = 1
    win1 += 1
  else:
    winner = 2
    win2 += 1
  print("Round %i: %i vs %i -> Hand %i wins" %(round, hand1[round], hand2[round], winner))
  if win1 > win2:
    finalWinner = 1
  else:
    finalWinner = 2
  print("Hand %s wins!" %finalWinner) #Level 4
