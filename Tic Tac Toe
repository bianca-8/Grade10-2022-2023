import pygame

pygame.init()        #initialize pygame
SIZE = (600, 600)    #screen size
screen = pygame.display.set_mode(SIZE)

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

# WRITE YOUR CODE HERE.
pygame.draw.line(screen,WHITE,(200,0),(200,600))
pygame.draw.line(screen,WHITE,(400,0),(400,600))
pygame.draw.line(screen,WHITE,(0,200),(600,200))
pygame.draw.line(screen,WHITE,(0,400),(600,400))
pygame.display.flip() 
pygame.time.wait(1000)

pygame.draw.circle(screen,BLUE,(100,100),80) #O1
pygame.display.flip() 
pygame.time.wait(1000)

pygame.draw.line(screen,RED,(200,200),(400,400),5)
pygame.draw.line(screen,RED,(400,200),(200,400),5) #X1
pygame.display.flip() 
pygame.time.wait(1000)

pygame.draw.circle(screen,BLUE,(500,500),80) #O2
pygame.display.flip() 
pygame.time.wait(1000)

pygame.draw.line(screen,RED,(0,200),(200,400),5)
pygame.draw.line(screen,RED,(200,200),(0,400),5) #X2
pygame.display.flip() 
pygame.time.wait(1000)

pygame.draw.circle(screen,BLUE,(500,300),80) #O3
pygame.display.flip() 
pygame.time.wait(1000)

pygame.draw.line(screen,RED,(400,0),(600,200),5)
pygame.draw.line(screen,RED,(600,0),(400,200),5) #X3
pygame.display.flip() 
pygame.time.wait(1000)

pygame.draw.circle(screen,BLUE,(300,500),80) #O4
pygame.display.flip() 
pygame.time.wait(1000)

pygame.draw.line(screen,RED,(0,400),(200,600),5)
pygame.draw.line(screen,RED,(200,400),(0,600),5) #X4
pygame.display.flip() 
pygame.time.wait(1000)

pygame.draw.line(screen,WHITE,(0,600),(600,0),10) #Win line
pygame.display.flip() 
pygame.time.wait(1000)

pygame.display.flip()   #display the drawing on screen
pygame.time.wait(3000)  #time to display in milliseconds
pygame.quit()
