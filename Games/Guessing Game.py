"""
Write a program that acts like a guessing game.  Your program should randomly choose a number between 1 and 100, then have the user try to guess the number in the fewest guesses.  After each incorrect guess, the program should respond with either “Too high” or “Too low”.
"""

import random

number = random.randint(1,100)
count = 0

while True:
  guess = int(input("Guess the number: "))
  count += 1
  if number > guess:
    print("Too low")
  elif number < guess:
    print("Too high")
  else:
    print("Good job, you guessed the number in %i tries!" %count)
    break
