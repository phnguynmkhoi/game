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

#set caption and icon and image
pygame.display.set_caption("Game cua Khoi")
icon = pygame.image.load('img/car.png')
pygame.display.set_icon(icon)
arrow = pygame.image.load('img/arrow.png')


#Background
class BACKGROUND:
    def __init__(self,img, start,end) :
        self.img=img
        self.start=start
        self.end=end
        self.car=[]

bg=[] 
bg.append (BACKGROUND(pygame.transform.scale(pygame.image.load('img/bg1.png'),(WIDTH,HEIGHT)),200,1000))
bg.append (BACKGROUND(pygame.transform.scale(pygame.image.load('img/bg2.png'),(WIDTH,HEIGHT)),0,1000))
bg.append (BACKGROUND(pygame.transform.scale(pygame.image.load('img/bg3.png'),(WIDTH,HEIGHT)),0,1000))
bg.append (BACKGROUND(pygame.transform.scale(pygame.image.load('img/bg4.png'),(WIDTH,HEIGHT)),0,800))

#Car
class CAR:
    def __init__(self, img, car_y ,velocity,curRound):
        self.img = pygame.transform.scale(img,(WIDTH/12.5,HEIGHT/12))
        self.x = 0
        self.y = car_y
        self.velocity = velocity
        self.destination = 0
        self.curRound=curRound

        # self.ratio=ratio
    def run(self):
        self.x += self.velocity
    
car=[]
des = int(WIDTH/1.25)
car.append(CAR(pygame.image.load('img/0_red_formulaOne.png'), int(HEIGHT/1.65), random.uniform(2,3), 0))
car.append(CAR(pygame.image.load('img/0_yellow_formulaOne.png'), int(HEIGHT/1.47), random.uniform(2,3), 0))
car.append(CAR(pygame.image.load('img/0_blue_formulaOne.png'), int(HEIGHT/1.32), random.uniform(2,3), 0))
car.append(CAR(pygame.image.load('img/0_pink_formulaOne.png'), int(HEIGHT/1.19), random.uniform(2,3), 0))
car.append(CAR(pygame.image.load('img/0_white_formulaOne.png'), int(HEIGHT/1.1),random.uniform(2,3), 0))

#setting CAR1
w = int(WIDTH/8)
h = int(HEIGHT/1.65)
player1_car = CAR(CAR1, w, h, random.uniform(1,1.5), des)

#setting CAR2
w = int(WIDTH/9)
h = int(HEIGHT/1.47)
player2_car = CAR(CAR2, w, h, random.uniform(1,1.5), des)

#setting CAR3
w = int(WIDTH/9)
h = int(HEIGHT/1.31)
player3_car = CAR(CAR3, w, h, random.uniform(1,1.5), des)

#setting CAR4
w = int(WIDTH/9)
h = int(HEIGHT/1.19)
player4_car = CAR(CAR4, w, h, random.uniform(1,1.5), des)

#setting CAR5
w = int(WIDTH/9)
h = int(HEIGHT/1.1)
player5_car = CAR(CAR5, w, h, random.uniform(1,1.5), des)

#gold
gold = 0
font = pygame.font.Font('freesansbold.ttf',30)
text = font.render(str(gold), True, white)
textPosition = text.get_rect()
textPosition.center = (WIDTH/22, HEIGHT/25)
coin_image = pygame.image.load('coin.png')
coin_image = pygame.transform.scale(coin_image, (WIDTH/30, HEIGHT/15))

#setting run
def draw(player_car):   
    screen.blit(player_car.img,(player_car.car_x, player_car.car_y))
    
#game Loop
clock = pygame.time.Clock()
fps = 60
count = 0

#Initalize
r=0
selected=0
pressed=0
for i in range (5):
    bg[r].car.append(i)
    car[i].x=bg[r].start
    car[i].curRound=r

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
        if event.type == pygame.KEYDOWN:
            print (event.key)
            pressed=1
            if event.key==pygame.K_F1:
                selected=0
            if event.key==pygame.K_F2:
                selected=1
            if event.key==pygame.K_F3:
                selected=2
            if event.key==pygame.K_F4:
                selected=3
            if event.key==pygame.K_F5:
                selected=4
        if event.type == pygame.KEYUP:
            pressed=0

    #draw 5 car
    for i in bg[car[selected].curRound].car:
        draw(car[i].img,car[i].x,car[i].y)

    if pressed ==1:
        for i in bg[car[selected].curRound].car:
            if i==selected :
                draw(arrow,car[i].x+10,car[i].y-45)
    #check if the car have finish the race
    for i in range (5):
        if car[i].x<=bg[car[i].curRound].end:
            car[i].run()
        elif car[i].curRound<3: 
            bg[car[i].curRound].car.remove(i)
            car[i].curRound+=1
            bg[car[i].curRound].car.append(i)
            car[i].x=bg[car[i].curRound].start-100

    
        #resize display
        # if event.type == VIDEORESIZE:
            
        #     screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        #     background = pygame.transform.scale(background,(event.w,event.h))

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