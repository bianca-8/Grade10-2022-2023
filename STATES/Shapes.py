from pygame import *
import pygame   
init()
# defining colours
RED = (255, 0, 0)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# defining the screen
SIZE = (800, 600)
screen = display.set_mode(SIZE)

# Three different stages
STATEONE = 1  # Draws just the background
STATETWO = 2  # Draws a border and background
STATETHREE = 3  # Draws an ellipse inside the border and background


def getNewState(button, curState):
  if curState == STATEONE and button == 1:
    curState = STATETWO 
  elif curState == STATETWO and button == 1: 
    curState = STATETHREE
  else:
    curState = STATEONE

  return curState



def drawScene(curState):
  # why are we only using if statements, not if else statements?
  if curState == STATEONE:
    draw.rect(screen, RED, (0, 0, 800, 600)) # background drawing
  if curState == STATETWO:
    draw.rect(screen, GREEN, (50, 50, 700, 500)) # border of width 50 pixels
  if curState == STATETHREE:
    draw.ellipse(screen, BLUE, (50, 50, 700, 500)) # inscribe the ellipse
  display.flip()



state = STATEONE  # initial state
running = True    # set our loop boolean
while running == True:
  drawScene(state)    # draw the scene given the current state
    
  for e in event.get():
    if e.type == QUIT:
      running = False
    if e.type == MOUSEBUTTONDOWN:
      button = e.button
      state = getNewState(button, state)
                
quit()
