# See question on Brightspace --> Unit 4 Loops --> Review
# Complete all the levels here.

sentence = input("Please enter a sentence: ")

letter = ""
space = ""
newLet = ""
even = ""
odd = ""
place = 0

#Level 2
for i in sentence:
  newLet = newLet + i
  if i == " ":
    newLet = newLet[:-1] + "mouse"
  letter = letter + " " + i + "(" + str(place) + ")"
  place += 1
  if i == " ":
    space = space + " " + str(place-1)

print(letter[1:])
print()
place = 0

#Level 3
print("Spaces are at locations: %s" %space[1:])
print()

#Level 4
print(newLet)
print()

#Level 4+
for i in newLet:
  if place % 2 == 0:
    even = even + i
  else:
    odd = odd + i
  place += 1
print("Even string is: %s" %even)
print("Odd string is: %s" %odd)
