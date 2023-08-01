# See question on Brightspace --> Unit 4 Loops --> Review
# Complete all levels here.

import random

animals = random.randrange(5,20)
print("The number of animals is %i." %animals)

total = animals + animals * 2
animalCount = animals
food = 1000
count = 1

while food > animalCount:
  food = food - animalCount + 4000
  animals *= 2
  print(count,animals,total,food)
  animalCount = total
  total += animals * 2
  count += 1
