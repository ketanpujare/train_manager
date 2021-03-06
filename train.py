# -*- coding: utf-8 -*-
import pygame

#pygame.display.init()

display_width = 1200
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
grey = (169,169,169)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Train Manager')
clock = pygame.time.Clock()



def signal(x,y,color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x-10 < mouse[0] < x+10 and y-10 < mouse[1] < y+10 and click[0]==1:
        color = red

    pygame.draw.circle(gameDisplay,color,(x,y),10)
     


gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameDisplay.fill(white)
    signal(100,100,green)
    signal(100,120,red)


    pygame.display.update()
    clock.tick(60)