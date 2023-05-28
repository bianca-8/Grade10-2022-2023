# See challenge on Brightspace
import random
from random import *
from pygame import*
init()
screen = display.set_mode((800, 500))
myClock = time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

draw.rect(screen,WHITE,(0,0,800,500))
draw.line(screen,BLACK,(400,0),(400,500))

myFont = font.SysFont("Times New Roman",30)
seconds = 0

pegLengths = []
for i in range(1,51):
  pegLengths.append(i*5)

shuffle(pegLengths)
pegs1 = pegLengths[:25]
pegs2 = pegLengths[25:]

while True:
  draw.rect(screen,WHITE,(0,0,800,500))
  draw.line(screen,BLACK,(400,0),(400,500))
  
  x = 405
  for peg in pegs1:
    draw.rect(screen,RED,(x,400-peg,5,peg))
    x+=10
  x = 390
  for peg in pegs2: 
    draw.rect(screen,RED,(x,400-peg,5,peg))
    x-=10

  text = myFont.render(str(seconds), 1, BLACK)
  screen.blit(text, (675,50,400,100))
  
  display.flip()
  if pegs1 == [] or pegs2 == []:
    break
  myClock.tick(30)
  
  if pegs1[0] > pegs2[0]:
    if randint(0,1) == 1:
      pegs1.append(pegs1[0])
      pegs1.append(pegs2[0])
    else:
      pegs1.append(pegs2[0])
      pegs1.append(pegs1[0])
  else:
    if randint(0,1) == 1:
      pegs2.append(pegs1[0])
      pegs2.append(pegs2[0])
    else:
      pegs2.append(pegs2[0])
      pegs2.append(pegs1[0])
  pegs1 = pegs1[1:]
  pegs2 = pegs2[1:]
  seconds += 1
    
display.flip()
time.wait(10000)

quit()

"""
print the pegs with one list going to the left of the black line 
print another with the list following to the right of the black line 
have a while running loop with an if statement to break 
for loops to print each peg list 
display after for loops, if statement to determine which peg is larger 
append those two pegs to the winner list, and remove them from the start 
"""
