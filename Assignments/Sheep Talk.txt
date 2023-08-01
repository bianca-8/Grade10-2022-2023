import random

#Level 2 ===============

def level2(string):
  for i in string:
    if i == "A":
      print("B")
    if i == "B":
      print("AB")
  
#Level 3 ===============
def level3(string):
  for i in string:
    if i == "A":
      print("B")
    if i == "B":
      print("AB")

#Level 4 ===============

def level4(string):
  output1 = ""
  output2 = ""
  for i in string:
    if i == "A":
      output1 = output1 + "B"
    if i == "B":
      output1 = output1 + "AB"
    
  for j in output1:
    if j == "A":
      output2 = output2 + "B"
    if j == "B":
      output2 = output2 + "AB"
        
  print(output1)
  print(output2)
  
#Level 4+ ==============

def level4Plus():
  string = "A"
  output = ""
  count = 1
  print(string)
  for i in string:
    if i == "A":
      output = output + "B"
    if i == "B":
      output = output + "AB"
  print(output)
  for x in range(6):
    for k in output:
      if k == "A":
        output = output[count:] + "B"
      if k == "B":
        output = output[count:] + "AB"
    print(output)


#=======================

randomString = ""
for i in range(7):
  randomString = randomString + random.choice(["A","B"])

level2("ABBA")
level3(randomString)
level4(randomString)
level4Plus()
