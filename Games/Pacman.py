import pygame

pygame.init()        #initialize pygame
xCoordinate = 500
yCoordinate = 500
SIZE = (xCoordinate, yCoordinate)    #screen size
screen = pygame.display.set_mode(SIZE)

# WRITE YOUR CODE HERE.
YELLOW = (241, 245, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

x = 0
y = 220

pygame.draw.ellipse(screen,YELLOW,(x,y,200,200), 100) #circle
pygame.draw.ellipse(screen,WHITE,(x,y,201,201),5) #outline
pygame.draw.polygon(screen,BLACK, ((x+100,y+100),(x+200,y+180), (x+200,y+30))) #mouth
pygame.draw.line(screen,WHITE,(x+100,y+100),(x+175,y+165),5)
pygame.draw.line(screen,WHITE,(x+100,y+100),(x+180,y+40),5) #outline of mouth
pygame.draw.circle(screen,BLACK,(x+120,y+60),10,10)
pygame.display.flip()
pygame.time.wait(1000)

times = int(xCoordinate/100)

for xCoordinate in range(times):
  #Mouth Open
  #Black Screen
  pygame.draw.rect(screen,BLACK,(0,0,500,500)) 
  pygame.display.flip()
  pygame.time.wait(1)

  x += 50
  
  pygame.draw.ellipse(screen,YELLOW,(x,y,200,200), 100) #circle
  pygame.draw.ellipse(screen,WHITE,(x,y,201,201),5) #outline
  pygame.draw.line(screen,WHITE,(x+100,y+100),(x+200,y+100),5)
#outline of mouth
  pygame.draw.circle(screen,BLACK,(x+120,y+60),10,10) #eye
  pygame.display.flip()
  pygame.time.wait(1000)

  #Mouth Closed
  #Black Screen
  pygame.draw.rect(screen,BLACK,(0,0,500,500)) 
  pygame.display.flip()
  pygame.time.wait(1)

  x += 100
  
  pygame.draw.ellipse(screen,YELLOW,(x,y,200,200), 100) #circle
  pygame.draw.ellipse(screen,WHITE,(x,y,201,201),5) #outline
  pygame.draw.polygon(screen,BLACK, ((x+100,y+100),(x+200,y+180), (x+200,y+30))) #mouth
  pygame.draw.line(screen,WHITE,(x+100,y+100),(x+175,y+165),5)
  pygame.draw.line(screen,WHITE,(x+100,y+100),(x+180,y+40),5) #outline of mouth
  pygame.draw.circle(screen,BLACK,(x+120,y+60),10,10) #eye
  pygame.display.flip()
  pygame.time.wait(1000)


pygame.display.flip()   #display the drawing on screen
pygame.time.wait(3000)  #time to display in milliseconds
pygame.quit()
