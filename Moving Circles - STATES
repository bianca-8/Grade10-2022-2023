"""
Modify this code to have the circle move left and right on the screen.
"""
from pygame import *
import pygame   

init()
SIZE = (400, 400)
screen = display.set_mode(SIZE)

RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

myClock = time.Clock()

#giving a CONSTANT name to these states
#using names for states is easy to remember
#Otherwise I have to remember which is T and which is F
STATEUP = True     
STATEDOWN = False  
STATERIGHT = True     
STATELEFT = False 
# if I have more than two states
#I would probably use the integers 0, 1, 2, etc...

# state is the actual variable that represents
# the current state
currentState = STATEUP
currentState1 = STATERIGHT

#starting values for the circle
posx = 200
posy = 200
posx1 = 200
posy1 = 200

while True:
  # drawing my background and circle
  draw.rect(screen, WHITE, (0, 0, 400, 400))
  draw.circle(screen, RED, (posx,posy), 20)
  display.flip()
  #time.wait(10)
  # move the circle
  if currentState == STATEUP:  # are we going up?
    posy -= 1         # move the circle up
    if posy <=20:      # about to move off the screen
      currentState = STATEDOWN  # change the state to move down
  else:                 # not going up, must be going down
    posy += 1         # move the circle down
    if posy >= 380:   # about to move off the screen
      currentState = STATEUP    # change the state to move up

  #2ND CIRCLE
  # drawing my background and 2nd circle
  draw.circle(screen, RED, (posx1,posy1), 20)
  display.flip()
  #time.wait(10)
  # move the circle
  if currentState1 == STATERIGHT:  # are we going up?
    posx1 -= 1         # move the circle up
    if posx1 <=20:      # about to move off the screen
      currentState1 = STATELEFT  # change the state to move down
  else:                 # not going up, must be going down
    posx1 += 1         # move the circle down
    if posx1 >= 380:   # about to move off the screen
      currentState1 = STATERIGHT    # change the state to move up
          
  myClock.tick(60)
  
quit()
