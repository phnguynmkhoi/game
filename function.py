from os import rename
import pygame,sys,ioexcel,random
import click, newdraw, try_nam,maingameplay,lichsuchoi
from pygame.constants import MOUSEBUTTONDOWN
from pygame.time import Clock
from pygame import mixer

pygame.init()

clock = pygame.time.Clock()

char_name = ''
chedo = 0

def main_menu(screen,username,selection_main_mennu = 0):
    WIDTH,HEIGHT = screen.get_size()
    tile = WIDTH/1920

    class Player(pygame.sprite.Sprite):
        def __init__(self, pos_x, pos_y):

            car0=pygame.image.load('img/background-menus/f1/0-f1.png')
            car0= pygame.transform.scale(car0, (700*tile, 300*tile))
            car1=pygame.image.load('img/background-menus/f1/1-f1.png')
            car1= pygame.transform.scale(car1, (700*tile, 300*tile))
            car2=pygame.image.load('img/background-menus/f1/2-f1.png')
            car2= pygame.transform.scale(car2, (700*tile, 300*tile))
            car3=pygame.image.load('img/background-menus/f1/3-f1.png')
            car3= pygame.transform.scale(car3, (700*tile, 300*tile))
            
            super().__init__()
            self.attack_animation = False
            self.sprites = []
            self.sprites.append(car0)
            self.sprites.append(car1)
            self.sprites.append(car2)
            self.sprites.append(car3)

            self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]

            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x,pos_y]

        def attack(self):
            self.attack_animation = True

        def update(self,speed):
            if self.attack_animation == True:
                self.current_sprite += speed
                if int(self.current_sprite) >= len(self.sprites):
                    self.current_sprite = 0
                    self.attack_animation = False

            self.image = self.sprites[int(self.current_sprite)]

    moving_sprites = pygame.sprite.Group()
    player = Player(200*tile,750*tile)
    moving_sprites.add(player)

    class BackgrounD: 
        def __init__(self):
            background = pygame.image.load('Image/menugame2.png')
            background = pygame.transform.scale(background,(background.get_width(),HEIGHT))
            self.x = 0
            self.y = 0
            self.speed = 3
            self.img = background
            self.width = self.img.get_width()
            self.height = self.img.get_height()
        def draw(self,surface):
            surface.blit(self.img,(self.x,self.y))
            surface.blit(self.img, (self.x - self.width,self.y))
        def update(self):
            self.x += self.speed
            if self.x > self.width:
                self.x -= self.width

    Background = BackgrounD()
    
    class leaf: 
            def __init__(self):
                image = pygame.image.load('banner/dollar.png').convert_alpha()
                self.image = pygame.transform.scale(image,(70*tile,70*tile))

                random_x_y = random.randint(1,2)
                if random_x_y == 1:
                    self.y = 0
                    self.x = random.randrange(0,int(WIDTH))
                else:
                    self.x = WIDTH
                    self.y = random.randint(0,int(HEIGHT))

                speed = round(random.uniform(5,5.5),2)
                self.speed = pygame.math.Vector2(-speed,speed)
                
                self.angle = random.randint(20,70)

                self.angle_change =  random.randrange(-1,1)

            def move(self,Surface):
                image = pygame.transform.rotozoom(self.image,self.angle,1)
                self.angle += self.angle_change
                self.x -= self.speed.x 
                self.y += self.speed.y
                image_rect = image.get_rect(center = (self.x,self.y))
                Surface.blit(image,image_rect)


    Leaf = []
    
    for i in range (0,21):
        Leaf.append(leaf())

    for i in range(0,21):
        Leaf[i].x = random.randrange(0,int(WIDTH))
        Leaf[i].y = random.randrange(0,int(WIDTH))
        

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.main_menu(screen, username, 0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selection_main_menu > 1:
                        selection_main_menu -= 1
                    print(selection_main_menu)        
                if event.key == pygame.K_DOWN:
                    if selection_main_menu < 5:
                        selection_main_menu += 1
                    print(selection_main_menu)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: pygame.quit()
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE:
                    if selection_main_menu == 1:
                        #choose_set(screen,0,0)
                        pass
                    if selection_main_menu == 2:
                        print('History')
                    if selection_main_menu == 3:
                        print('Options')
                    if selection_main_menu == 4:
                        print('Help')
                    if selection_main_menu == 5:
                        pygame.quit()

        newdraw.main_menu(screen, selection_main_mennu,Leaf,Background,moving_sprites,player)
        pygame.display.update()
        clock.tick(144)

def choose_minigame(screen, username, selection_mini):
    global mode
    while True:
        cost = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ioexcel.writeExcel()
                pygame.quit()
                sys.exit()
                
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_RIGHT  or event.key == pygame.K_LEFT and selection_mini==0:
            #         selection_mini += 1
            #         print (selection_mini)
            #     if event.key == pygame.K_LEFT  or event.key == pygame.K_LEFT and selection_mini==1: 
            #         selection_mini -= 1
            #         print (selection_mini)
            if event.type==pygame.MOUSEBUTTONDOWN:
                click.choose_minigame(screen,username,selection_mini)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER: main_menu(screen, selection_main_menu = 0)
            
        newdraw.choose_minigame(screen,username, selection_mini)
        pygame.display.update()
        clock.tick(100)

def choose_track(screen, username, selection_track):
    global mode
    while True:
        cost = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ioexcel.writeExcel()
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.choose_track(screen, username,selection_track)

                
            #click.choose_track(screen, username,selection_track)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and selection_track<5:
                    selection_track += 1
                    print (selection_track)
                if event.key == pygame.K_LEFT and selection_track>1: 
                    selection_track -= 1
                    print (selection_track)
                if event.key == pygame.K_UP and selection_track ==4:
                    selection_track = 0
                    print(selection_track)
                if event.key == pygame.K_UP and selection_track ==5:
                    selection_track = 1
                    print(selection_track)      
                if event.key == pygame.K_DOWN and selection_track == 1:
                    selection_track = 2
                    print(selection_track)
                if event.key == pygame.K_DOWN and selection_track == 2:
                    selection_track = 3
                    print(selection_track)
                if event.key == pygame.K_DOWN and selection_track == 3:
                    selection_track = 4
                    print(selection_track)
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER: main_menu(screen, selection_main_menu = 0)
                
        newdraw.choose_track(screen,username, selection_track)
        '''
        newdraw.choose_set(screen, username, selection_set, selection_char)
        newdraw.choose_char(screen, selection_set, selection_char)
        newdraw.money(screen, username)
        if minigame != 0: 
            newdraw.minigame(screen, username)
            '''
        pygame.display.update()
        clock.tick(100)

def choose_set(screen, username, selection_track,selection_set, selection_char):
    global mode
    while True:
        cost = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ioexcel.writeExcel()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.choose_set(screen, username,selection_track,selection_set,selection_char)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selection_char = 1
                    newdraw.choose_char(screen, selection_set, 1)
                if event.key == pygame.K_LEFT: 
                    selection_char = 0
                    newdraw.choose_char(screen,selection_set, 0)
                    
                if event.key == pygame.K_UP and selection_char == 0:
                    if selection_set > 0: selection_set -= 1
                    print(selection_set)  
                          
                if event.key == pygame.K_DOWN and selection_char == 4:
                    if selection_set < 4: selection_set += 1
                    print(selection_set)
                    
                if event.key == pygame.K_UP and selection_char != 0:
                    if selection_char > 0: selection_char -= 1 
                    print(selection_char)
                      
                if event.key == pygame.K_DOWN and selection_char != 0:
                    if selection_char < 4: selection_char += 1
                    print(selection_char)
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: main_menu(screen, selection_main_menu = 0)
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE:
                    if selection_char != -1 and selection_set != -1: 
                        choose_bet(screen, username, selection_set*10+selection_char, char_name, 0, 0, 0)

        newdraw.choose_set(screen, username, selection_set, selection_char)
        newdraw.choose_char(screen, selection_set, selection_char)
        newdraw.money(screen, username)
        #if minigame != 0: 
            #draw.minigame(screen, username)
        pygame.display.update()
        clock.tick(100)

def choose_bet(screen, username, selection_track,set_char, char_name, rename, cost, mode):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ioexcel.writeExcel()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.bet(screen, username,selection_track, set_char, char_name, rename, cost, mode)
            if event.type == pygame.KEYDOWN:
                if rename == 1 and len(char_name) < 10:
                    if event.key == pygame.K_BACKSPACE:
                        char_name = char_name[:-1]
                    else:
                        char_name += event.unicode 
                if event.key == pygame.K_BACKSPACE:
                    char_name = char_name[:-1] 
        newdraw.choose_bet(screen,set_char,char_name, rename, cost, mode)
        newdraw.money(screen, username)
        pygame.display.update()
        clock.tick(60)

def store(screen, username, cart):
    WIDTH, HEIGHT = screen.get_size()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ioexcel.writeExcel()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                click.store(screen, username)
                
        cart = ioexcel.laymabua()
            
        newdraw.store(screen, username, cart)
        newdraw.money(screen, username)
        pygame.display.update()
        clock.tick(60)

def options(screen, username):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ioexcel.writeExcel()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                click.options(screen, username)
        
        newdraw.options(screen, username)
        pygame.display.update()
        clock.tick(60)

def history(screen, username):
    WIDTH, HEIGHT = screen.get_size()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ioexcel.writeExcel()
                pygame.quit()
                sys.exit()

        print(ioexcel.laythongtinhienthi(username))
        lichsuchoi.history(screen, username, WIDTH/1920, ioexcel.laythongtinhienthi(username))
        pygame.display.update()
        clock.tick(60)

def help(screen, username, selection_help, goback):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ioexcel.writeExcel()
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                click.help(screen, username, selection_help, goback)
        
        newdraw.help(screen, username, selection_help)
        pygame.display.update()
        clock.tick(60)

def score(screen, username, thongtin,tennv,nvcuoc,tile):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ioexcel.writeExcel()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click.score(screen, username, thongtin,tennv,nvcuoc,tile)
        if event.type == pygame.KEYDOWN: pass
    
    #maingameplay.game_over_situation(screen, username, thongtin,tennv,nvcuoc,tile)

def gameplay(screen, username,selection_track, set_char, char_name, rename, cost, mode):
    WIDTH, HEIGHT = screen.get_size()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ioexcel.writeExcel()
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click.bet(screen, username, selection_track,set_char, char_name, rename, cost, mode)
        if event.type == pygame.KEYDOWN:
            if rename == 1 and len(char_name) < 10:
                if event.key == pygame.K_BACKSPACE:
                    char_name = char_name[:-1]
                else:
                    char_name += event.unicode
    
    maingameplay.gameplaymain(screen,selection_track, username, str(set_char), char_name, cost, WIDTH/1920, mode)