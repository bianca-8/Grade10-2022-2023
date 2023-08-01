"""
Write a program that asks the users to input any 10 numbers.  Your program should then display the numbers in order from largest to smallest as well as the median.
"""
finalNum = []

for i in range(10):
  num = input("Please enter a number: ")
  finalNum += num
print(finalNum)

finalNum.sort(reverse = True)
print("Numbers from largest to smallest is %s." %finalNum)

median = (int(finalNum[4]) + int(finalNum[5])) / 2
print("Median is %s." %median)
