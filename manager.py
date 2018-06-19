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

# class Station:
#     def station(self,startx,starty,endx,endy,color=grey,width=7):
#         self.color = color
#         self.startx = startx
#         self.starty = starty        
#         self.endx = endx
#         self.endy = endy
#         self.width = width

#         pygame.draw.line(gameDisplay,color,(startx,starty),(endx,endy),width)


#Stations
train_stations = [['rn',2],['niv',3],['advi',1],['vrli',1],['vid',1],['sual',1],['rajp',3],['vbw',2],['nan',3],\
                  ['kkw',3],['sndd',3],['kudl',0]]

railline = []
for ts in train_stations:
    for i in range(ts[1]+1):
        railine_var = ts[0]+str(i)
        railline.append(railine_var)

#Rail Line & Signal Automation
rld = {}
signal_list = []
signal_d = {}
start  = 20
rly1   = 120
length = 40
signal_pos_from_x = 5
signal_pos_from_y = 15

for rl in railline:
    color = black
        
    #End of Screen
    if start >= 1150:
        start = 20
        rly1 = 220
    
    #Station Platform differentiation form Railline(Gray Color)
    if '0' in rl:
        color = grey
                
        #Signal Color Up
        su = rl+'su'
        signal_d[su] = [start+length+signal_pos_from_x,rly1-signal_pos_from_y,red]

        #Signal up Instances
        su = Signal()
        signal_list.append(su)

        #Signal Color Down
        sd = rl+'sd'
        signal_d[sd] = [start-signal_pos_from_x,rly1+signal_pos_from_y,red]

        #Signal Down Instances
        sd = Signal()
        signal_list.append(sd)



    rld[rl] = [start,rly1,start+length,rly1,color]
    start += length+10


#print rld
#print signal_d

#RailLine Instances
rl_list = []
station_list = []
for rl in railline:
    rl = Line()
    rl_list.append(rl)


#Game Loop
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameDisplay.fill(white)

    #Signals
    for sl,sc in zip(signal_list,signal_d):
        signal_d[sc][2] = sl.signal(signal_d[sc][0],signal_d[sc][1],signal_d[sc][2]) 
        # rn0sc   = rn0.signal(55,105,rn0sc)

    #RaiLine
    rlcolor = black
    rly1    = 120
    start   = 10
    length  = 40
    for rl,i in zip(rl_list,rld):
        rl.line(rld [i][0],rld [i][1],rld [i][2],rld [i][3],rld [i][4])
        #rn0.line(10,rly1,50,rly1,color)

    pygame.display.update()
    clock.tick(20)