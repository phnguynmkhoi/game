from turtle import width
import pygame
from pygame.locals import *
import math
import random
import time

pygame.init()

#set color
green = (76,208,56)
gray = (100,100,100)
red = (200,0,0)
yellow = (255,232,0)
white = (255,255,255)

#set screen
WIDTH=1000
HEIGHT=600  
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)

#set caption and icon
pygame.display.set_caption("Game cua Khoi")
icon = pygame.image.load('car.png')
pygame.display.set_icon(icon)

#Background
background = pygame.image.load('background-levels-city.png')
background = pygame.transform.scale(background,(WIDTH,HEIGHT))

#Car
Car1 = pygame.image.load('0_blue_formulaOne.png')
Car1 = pygame.transform.scale(Car1,(WIDTH/12.5,HEIGHT/12))
w_1 = int(WIDTH/9)
h_1 = int(HEIGHT/1.67777777)
destination = int(WIDTH/1.25)

#game Loop
clock = pygame.time.Clock()
fps = 120

running=True
while running:

    clock.tick(fps)     

    #setBackground
    screen.blit(background,(0,0))

    #draw the car
    screen.blit(Car1,(w_1,h_1))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        #resize display
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            background = pygame.transform.scale(background,(event.w,event.h))
            Car1 = pygame.transform.scale(Car1,(event.w/12.5,event.h/12))
            w_1 = int(event.w/9)
            h_1 = int(event.h/1.6777777)
    if (w_1 <= destination):
        w_1+=1
    

    pygame.display.update()

pygame.quit()