# -*- coding: utf-8 -*-
import threading
import pygame
import time

display_width = 1200
display_height = 600

black = (0,0,0)
white = (255,255,255)
red   = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
grey  = (169,169,169)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Train Manager')
clock = pygame.time.Clock()

e10103 = ['rn',blue]

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

class Line:
    def line(self,startx,starty,endx,endy,color=black,width=5):
        self.color = color
        self.startx = startx
        self.starty = starty        
        self.endx = endx
        self.endy = endy
        self.width = width

        pygame.draw.line(gameDisplay,color,(startx,starty),(endx,endy),width)

class Station:
    def station(self,startx,starty,endx,endy,color=grey,width=7):
        self.color = color
        self.startx = startx
        self.starty = starty        
        self.endx = endx
        self.endy = endy
        self.width = width

        pygame.draw.line(gameDisplay,color,(startx,starty),(endx,endy),width)
        


#UP Signals
srn10   = Signal()
srn11   = Signal()
skkw1   = Signal()
skudl1  = Signal()


srn10c   = red
srn11c   = red 
skkw1c   = red
skudl1c  = red

#Stations
train_stations = [['rn',4],['niv',3],['advi',4]]
railline = []
for i in train_stations:
    for train_station in range(1,i[1]+1):
        railine_var = i[0]+str(train_station)
        railline.append(railine_var)
        
print(railline)

#RailLines
rl_list = []

for rl in railline:
    rl = Line()
    rl_list.append(rl)


gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameDisplay.fill(white)

    #Signals
    srn10c   = srn10.signal(55,105,srn10c)
    srn11c   = srn11.signal(155,105,srn11c)
    skkw1c   = skkw1.signal(500,105,skkw1c)
    skudl1c  = skudl1.signal(800,105,skudl1c)

    #Stations


    #RaiLine
    rlcolor = black
    rly1    = 120
    start   = 10
    length  = 40
    for rl in rl_list:
        rl.line(start,rly1,start+length,rly1,black)
        start += length+10

    # rlrn10.line(10,rly1,50,rly1,rlcolor)


    pygame.display.update()
    clock.tick(20)