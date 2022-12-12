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
class Car:
    def __init__(self, img, car_x, car_y ,velocity, destination):
        self.img = img
        self.car_x = car_x
        self.car_y = car_y
        self.velocity = velocity
        self.destination = destination

#create Car
CAR1 = pygame.image.load('0_red_formulaOne.png')
CAR2 = pygame.image.load('0_yellow_formulaOne.png')
CAR3 = pygame.image.load('0_blue_formulaOne.png')
CAR4 = pygame.image.load('0_pink_formulaOne.png')
CAR5 = pygame.image.load('0_white_formulaOne.png')

#create item
ITEM = pygame.image.load('coin.png')
ITEM = pygame.transform.scale(ITEM,(WIDTH/12.5,HEIGHT/12))

#RESIZE CAR
CAR1 = pygame.transform.scale(CAR1,(WIDTH/12.5,HEIGHT/12))
CAR2 = pygame.transform.scale(CAR2,(WIDTH/12.5,HEIGHT/12))
CAR3 = pygame.transform.scale(CAR3,(WIDTH/12.5,HEIGHT/12))
CAR4 = pygame.transform.scale(CAR4,(WIDTH/12.5,HEIGHT/12))
CAR5 = pygame.transform.scale(CAR5,(WIDTH/12.5,HEIGHT/12))

#setting destination
des = int(WIDTH/1.25)

#setting CAR1
w = int(WIDTH/8)
h = int(HEIGHT/1.65)
player1_car = Car(CAR1, w, h, random.uniform(1,1.5), des)

#setting CAR2
w = int(WIDTH/9)
h = int(HEIGHT/1.47)
player2_car = Car(CAR2, w, h, random.uniform(1,1.5), des)

#setting CAR3
w = int(WIDTH/9)
h = int(HEIGHT/1.31)
player3_car = Car(CAR3, w, h, random.uniform(1,1.5), des)

#setting CAR4
w = int(WIDTH/9)
h = int(HEIGHT/1.19)
player4_car = Car(CAR4, w, h, random.uniform(1,1.5), des)

#setting CAR5
w = int(WIDTH/9)
h = int(HEIGHT/1.1)
player5_car = Car(CAR5, w, h, random.uniform(1,1.5), des)

#gold
gold = 0
font = pygame.font.Font('freesansbold.ttf',30)
text = font.render(str(gold), True, white)
textPosition = text.get_rect()
textPosition.center = (WIDTH/20, HEIGHT/25)
coin_image = pygame.image.load('coin.png')
coin_image = pygame.transform.scale(coin_image, (WIDTH/30, HEIGHT/15))

#setting run
def draw(player_car):   
    screen.blit(player_car.img,(player_car.car_x, player_car.car_y))
    
#game Loop
clock = pygame.time.Clock()
fps = 60
count = 0

running=True
while running:

    clock.tick(fps)     

    screen.blit(background,(0,0))
    screen.blit(text, textPosition)
    screen.blit(coin_image, (0,0))

    #draw 5 car
    draw(player1_car)
    draw(player2_car)
    draw(player3_car)
    draw(player4_car)
    draw(player5_car)

    #check if the car have finish the race
    if player1_car.car_x<=player1_car.destination:
        player1_car.car_x += player1_car.velocity

    if player2_car.car_x<=player2_car.destination:
        player2_car.car_x += player2_car.velocity

    if player3_car.car_x<=player3_car.destination:
        player3_car.car_x += player3_car.velocity

    if player4_car.car_x<=player4_car.destination:
        player4_car.car_x += player4_car.velocity

    if player5_car.car_x<=player5_car.destination:
        player5_car.car_x += player5_car.velocity

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        #resize display
        if event.type == VIDEORESIZE:
            
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            background = pygame.transform.scale(background,(event.w,event.h))

            #resize Car
            CAR1 = pygame.transform.scale(CAR1,(event.w/12.5,event.h/12))
            CAR2 = pygame.transform.scale(CAR2,(event.w/12.5,event.h/12))
            CAR3 = pygame.transform.scale(CAR3,(event.w/12.5,event.h/12))
            CAR4 = pygame.transform.scale(CAR4,(event.w/12.5,event.h/12))
            CAR5 = pygame.transform.scale(CAR5,(event.w/12.5,event.h/12))
            des = int(event.w/1.25)
            count+=1 
            if count % 2 == 1:
                player1_car.velocity = player1_car.velocity * 3060 / WIDTH 
                player2_car.velocity = player2_car.velocity * 3060 / WIDTH 
                player3_car.velocity = player3_car.velocity * 3060 / WIDTH 
                player4_car.velocity = player4_car.velocity * 3060 / WIDTH 
                player5_car.velocity = player5_car.velocity * 3060 / WIDTH
            else:
                player1_car.velocity = player1_car.velocity * WIDTH / 3060
                player2_car.velocity = player2_car.velocity * WIDTH / 3060 
                player3_car.velocity = player3_car.velocity * WIDTH / 3060 
                player4_car.velocity = player4_car.velocity * WIDTH / 3060 
                player5_car.velocity = player5_car.velocity * WIDTH / 3060

            #resize Car1
            w = int(event.w/8)
            h = int(event.h/1.65)
            player1_car = Car(CAR1, w, h, player1_car.velocity, des)
            
            #resize Car2
            w = int(event.w/9)
            h = int(event.h/1.47)
            player2_car = Car(CAR2, w, h, player2_car.velocity, des)
            
            #resize Car3
            w = int(event.w/9)
            h = int(event.h/1.31)
            player3_car = Car(CAR3, w, h, player3_car.velocity, des)
            
            #resize Car4
            w = int(event.w/9)
            h = int(event.h/1.19)
            player4_car = Car(CAR4, w, h, player4_car.velocity, des)
            
            #resize Car5
            w = int(event.w/9)
            h = int(event.h/1.1)
            player5_car = Car(CAR5, w, h, player5_car.velocity, des)


    pygame.display.update()

pygame.quit()