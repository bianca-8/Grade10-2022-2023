import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600,600))

PURPLE = (255,100,255)

x1 = 50
y1 = 483
x2 = 550
y2 = 483
x3 = 300
y3 = 50

randomX = random.randint(0,600)
randomY = random.randint(0,600)

def midpoint(x1, y1, x2, y2):
  x = (x1+x2) / 2
  y = (y1 + y2) / 2
  return x, y

pygame.draw.circle(screen, PURPLE, (x1,y1), 1)
pygame.draw.circle(screen, PURPLE, (x2,y2), 1)
pygame.draw.circle(screen, PURPLE, (x3,y3), 1)

for i in range(100000):
  point = random.randint(1,3)
  if point == 1:
    x, y = midpoint(randomX,randomY,x1, y1)
    pygame.draw.circle(screen, (random.randint(0,255),0,255), (x, y), 1)
  elif point == 2:
    x, y = midpoint(randomX,randomY,x2, y2)
    pygame.draw.circle(screen, (255,random.randint(0,255),0), (x, y), 1)
  else:
    x, y = midpoint(randomX,randomY,x3, y3)
    pygame.draw.circle(screen, (0,255,random.randint(0,255)), (x, y), 1)

  
  randomX, randomY = x, y
  
  pygame.display.flip()
  pygame.time.wait(1)

pygame.display.flip()
pygame.time.wait(5000000)
pygame.quit()
