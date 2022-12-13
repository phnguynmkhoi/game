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
WIDTH=1500
HEIGHT=800  
screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)

#set caption and icon
pygame.display.set_caption("Dua xe ca do")
icon = pygame.image.load('car.png')
pygame.display.set_icon(icon)

class Background(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(x, y))

    def update(self):
        screen.blit(self.image, (0,0))

#Create background group
background_group = pygame.sprite.Group()
background1 = Background("./background levels/background-city.png", WIDTH, HEIGHT)

#setting destination
des = 1380

#Define Classes
class Game:
    def __init__(self):
        '''Initialize the game'''
        pass

    def update(self):
        """Update the game"""
        pass

    def draw(self):
        """Draw the Hud and other information to display"""
        pass

    def car(self):
        """Car"""
        pass

    def check_collisions(self):
        """Check collisions between car and item"""
        pass

    def check_who_win(self):
        """Check who is the winner"""
        pass

    def start_new_game(self):
        """Like the name"""
        pass

    def pause_game(self):
        pass

class Car(pygame.sprite.Sprite):
    def __init__(self, image, x:float, y:float, velocity:float):
        '''Initialize the game'''
        super().__init__()
        self.sprite = [] 
        i = 0
        for i in range(0,3):
            self.sprite.append(pygame.transform.scale(pygame.image.load(image[i]) ,(WIDTH/11,HEIGHT/9)))
        self.current_image = 0
        self.image = self.sprite[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = velocity
        self.position = x

        car_group.add(self)

    def update(self):
        self.move()
        self.check_collisions()

    def move(self):
        """Move the car"""
        if self.rect.x <= des:
            self.current_image+=1
            if self.current_image >= len(self.sprite):
                self.current_image=0
            self.image = self.sprite[self.current_image]
            self.position += self.velocity
            self.rect.x = self.position
        

    def check_collisions(self):
        pass
        

class Item(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('./mics/mystery box.png') ,(WIDTH/24,HEIGHT/20))
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.uniform(200, des-50),y)
        item_group.add(self)

    def update(self):
        pass

#Create Car Group
car_group = pygame.sprite.Group()

#Create Item Group
item_group = pygame.sprite.Group()

#setting CAR1
w = 16
h = 402
vel = random.uniform(1,1.5)
player1_car = Car(['./formula ones/0_red_formulaOne.png', './formula ones/1_red_formulaOne.png', './formula ones/2_red_formulaOne.png'], w, h, vel)
item1 = Item(h+14)

#setting CAR2
w = 16
h = 485
vel = random.uniform(1,1.5)
player2_car = Car(['./formula ones/0_yellow_formulaOne.png', './formula ones/1_yellow_formulaOne.png', './formula ones/2_yellow_formulaOne.png'], w, h, vel)
item1 = Item(h+12)


#setting CAR3
w = 16
h = 568
vel = random.uniform(1,1.5)
player3_car = Car(['./formula ones/0_blue_formulaOne.png', './formula ones/1_blue_formulaOne.png', './formula ones/2_blue_formulaOne.png'], w, h, vel)
item1 = Item(h+10)

#setting CAR4
w = 16
h = 648
vel = random.uniform(1,1.5)
player4_car = Car(['./formula ones/0_pink_formulaOne.png', './formula ones/1_pink_formulaOne.png', './formula ones/2_pink_formulaOne.png'], w, h, vel)
item1 = Item(h+10)

#setting CAR5
w = 16
h = 727
vel = random.uniform(1,1.5)
player5_car = Car(['./formula ones/0_green_formulaOne.png', './formula ones/1_green_formulaOne.png', './formula ones/2_green_formulaOne.png'], w, h, vel)
item1 = Item(h+10)

    
#game Loop
clock = pygame.time.Clock()
FPS = 60

running=True
while running:    

    clock.tick(FPS) 

    Background.update(background1)

    #draw item
    item_group.draw(screen)

    #draw 5 car
    car_group.draw(screen)
    car_group.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()

        #resize display
        if event.type == VIDEORESIZE:
            
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            background = pygame.transform.scale(background,(event.w,event.h))

    #Update the display and tick the clock
    pygame.display.update()

pygame.quit()