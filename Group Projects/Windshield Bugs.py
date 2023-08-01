import pygame
import random
import math
def distance(x1,y1,x2,y2):
  return math.sqrt((x2-x1)**2 + (y1-y2)**2)

BLACK = (0,0,0)
RED = (255,0,0)
GREY = (100,100,100)
pygame.init()
screen = pygame.display.set_mode((600,600))

textFont = pygame.font.SysFont("Times New Roman", 12)
percentageFont = pygame.font.SysFont("Times New Roman", 40)
text = textFont.render("% bugs not cleared" , 1, BLACK)	


pygame.draw.rect(screen,GREY,(0,0,600,200))
pygame.draw.arc(screen,BLACK,(0,0,400,400),0, math.pi)
pygame.draw.line(screen, BLACK, (400,0), (400,200))
pygame.draw.rect(screen, RED, (400,150,200,50))
screen.blit(text, (425,170,200,50))
not_cleared = 0
for i in range(0,10000):
  x1 = random.randint(0,400)
  y1 = random.randint(0,200)
  pygame.draw.circle(screen,RED,(x1,y1),1)
  pygame.display.flip()
  if distance(x1, y1, 200, 200) > 200:
    not_cleared +=1



percentageNotCleared = (not_cleared / 10000) * 100
percentage = "%.2f%%" %(percentageNotCleared)
percentText = percentageFont.render(percentage, 1, BLACK)	
screen.blit(percentText, (430,60,200,50))

pygame.display.flip()
pygame.time.wait(5000000)
pygame.quit()
