# See challenge on Brightspace
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

time = 0

# creating list of stairs
stairs = [random.randint(1,3)]
for i in range(0,19):
  stairs.append(0)

#defining fonts
myFont = pygame.font.SysFont("Times New Roman", 30)
pygame.draw.rect(screen,WHITE,(0,0,600,400))

# stairs
x = 0
y = 300
while x < 600:
  pygame.draw.rect(screen,BLACK,(x,y,30,5))
  x +=30
  y -=5
  
while True:
   
  #time
  pygame.draw.rect(screen,WHITE,(400,100,100,50))
  text = myFont.render(str(time), 1, BLACK)
  screen.blit(text, (400,100,400,100))
  time += 1
  # for loop for stairs 
  x = 0
  y = 300
  for i in range(0,20):
    if stairs[i] == 0:
      pygame.draw.line(screen,WHITE,(x+15,y-1),(x+15,y-20),3)
    if stairs[i]==1:
      pygame.draw.line(screen,RED,(x+15,y-1),(x+15,y-20),3)
      # pygame.draw.line(screen,WHITE,(x-15,y+4),(x-15,y-20),3)
    elif stairs[i]==2:
      pygame.draw.line(screen,GREEN,(x+15,y-1),(x+15,y-20),3)
      #pygame.draw.line(screen,WHITE,(x-15,y+4),(x-15,y-20),3)
    elif stairs[i]==3:
      pygame.draw.line(screen,BLUE,(x+15,y-1),(x+15,y-20),3)
      #pygame.draw.line(screen,WHITE,(x-15,y+4),(x-15,y-20),3)
    x += 30
    y -= 5
  stairs=[random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3])]+stairs[0:-1]
  pygame.display.flip()
  pygame.time.wait(1000)
  
  if stairs == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
    break


pygame.display.flip()
pygame.time.wait(10000)
pygame.quit()
