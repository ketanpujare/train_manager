# -*- coding: utf-8 -*-
import pygame

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


class Signal:
    def signal(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x-10 < mouse[0] < x+10 and y-10 < mouse[1] < y+10 and click[2]==1 and color == red:
            color = green
            pygame.draw.circle(gameDisplay,color,(x,y),10)
            #print('RED')
        elif x-10 < mouse[0] < x+10 and y-10 < mouse[1] < y+10 and click[0]==1 and color == green:
            color = red
            pygame.draw.circle(gameDisplay,color,(x,y),10)
            #print('green')
        pygame.draw.circle(gameDisplay,color,(x,y),10)
        
        return color

#UP Signals
rn1   = Signal()
kkw1  = Signal()
kudl1 = Signal()

rn1c  = red
kkw1c  = red
kudl1c = red

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameDisplay.fill(white)

    rn1c   = rn1.signal(100,100,rn1c)
    kkw1c  = kkw1.signal(500,100,kkw1c)
    kudl1c = kudl1.signal(800,100,kudl1c)

    pygame.display.update()
    clock.tick(20)