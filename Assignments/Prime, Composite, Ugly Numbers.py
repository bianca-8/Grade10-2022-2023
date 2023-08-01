"""
Write a program that reads an unknown number of numbers from the file called random.dat.  Output how many of the numbers are:

a)	prime numbers
b)	composite numbers (not primes)
c)	ugly numbers (any number who has only the prime factors of 2, 3 and 5)
"""

file = (open("random.dat", "r"))
composite = 0
prime = 0
ugly = 0

while True:
  text = file.readline()
  text = text.rstrip("\n")
  
  if text == "":
    break

  text = int(text)
  
  for i in range(1, text):
    if text % i == 0 and i != 1: #composite
      composite += 1
      break
    if text - 1 == i: #prime
      prime += 1
      break

    if text % 2 == 0 and text % 3 == 0 and text % 5 == 0:
      ugly += 1

print("Prime:", prime)
print("Composite:", composite)
print("Ugly:", ugly)

file.close()
