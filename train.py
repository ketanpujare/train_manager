# -*- coding: utf-8 -*-
import pygame

pygame.display.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Train Manager')
clock = pygame.time.Clock()

trainImg = pygame.image.load('blue.png')

def train(x,y):
    gameDisplay.blit(trainImg,(x,y))

x = 100
y = 200

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    gameDisplay.fill(white)
    train(x,y)

    pygame.display.update()
    clock.tick(60)
