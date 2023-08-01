"""
Write a program that asks the user to input five names.  Your program should output the names alphabetically.
"""
list = []

for i in range(5):
  name = input("Please enter a name: ")
  list.append(name)
  list.sort()
print(list)
