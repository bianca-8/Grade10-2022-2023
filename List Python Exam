# READ PART D - PROGRAMMING QUESTION ON BRIGHTSPACE --> EXAM
# ONLY BRIGHTSPACE TAB AND REPLIT TAB SHOULD BE OPEN

list = []
occurences = []

str = input("Please enter a string: ")
for i in str:
  list.append(i)

print(list) #Level 2


str = str.lower()
newList = []

for i in str:
  if newList.count(i) == 0:
    newList.append(i)
    occurences.append(1)
  else:
    place = newList.index(i)
    occurences[place] += 1

print(newList) #Level 3
print(occurences) #Level 4
print()


str2 = input("Please enter a second string: ")
substring = ""

if len(str) > len(str2): #str longer
  for chr in range(len(str)):
    for index in range(len(str2)):
      if str2[index] == str[chr]:
        substring += str2[index]
        break
else: #str2 longer
  for chr2 in range(len(str2)):
    for index2 in range(len(str)):
      if str[index2] == str2[chr2]:
        substring += str[index2]
        break

print(substring) #Level 4+
