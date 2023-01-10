import pygame,sys, function

from pygame.constants import MOUSEBUTTONDOWN
from pygame import mixer
import ioexcel
pygame.init()

default_width = 1920
default_height = 1080
click_sound = mixer.Sound('Music/click.mp3')

thongtin = ('haha', 2150, 11, 5, 6, ['', '1', '0', '1', '0', '0', '0', '1', '1', '0', '0', '1'], ['', '35', '25', '14', '20', '31', '31', '41', '41', '32', '32', '33'], ['', '+500', '-300', '+200', '-150', '-200', '-200', '+300', '+300', '-300', '-300', '+300'])

def history(screen, username, tyle, thongtin):

    class Table_of_information:
        def __init__(self,ten,tongtien,tyle):
            self.Text = 'Name: ' + ten + '  --  Money: ' + str(tongtien)
            self.font = pygame.font.Font('Font/LG.otf',int(70*tyle))
        def draw(self,Surface,tyle):
            Text_surface = self.font.render(self.Text,True,pygame.Color('Orange'))
            Text_rect = Text_surface.get_rect(topleft = (20*tyle,20*tyle))
            Surface.blit(Text_surface,Text_rect)

    class Table_of_match:
        def __init__(self,match,win,loss):
            self.Text = 'Match/Win/Lose: ' + str(match) + '/' + str(win) + '/' + str(loss)
            self.font = pygame.font.Font('Font/LG.otf',int(70*tyle))
        def draw (self,Surface,tyle):
            Text_surface = self.font.render(self.Text,True,pygame.Color('Orange'))
            Text_rect = Text_surface.get_rect(topright = ((default_width-20)*tyle,20*tyle))
            Surface.blit(Text_surface,Text_rect)

    class Table_of_match_status:
        def __init__(self,thongtin,index,starter_point,tyle):
            self.thongtin = thongtin
            self.index = index - starter_point
            self.match = index
            self.font = pygame.font.Font('Font/GEO_AI__.TTF',int(70*tyle))
        def draw (self,Surface,tyle):
            Table = pygame.Rect(400*tyle,(180*(self.index+1)+100)*tyle,1120*tyle,150*tyle)

            Match = self.match 
            if self.thongtin[0] == '1':
                Result = 'Win'
            else: Result = 'Lose'

            Change = self.thongtin[2]
            Character = self.thongtin[1]

            Text1 = str(Match) + '.' + Result
            Text2 = Change
            Text3 = Character
            if len(Character)==2:
                ava = pygame.image.load('Image/Gameplay/set'+ Character[0] + '/car'+ Character[1]+'.png')
            else:
                ava = pygame.image.load('Image/Gameplay/car'+ Character[0]+'.png')
            ava = pygame.transform.scale(ava, (tyle*250,tyle*100))
            
            Text1_surface = self.font.render(Text1,True,pygame.Color('black'))
            Text2_surface = self.font.render(Text2,True,pygame.Color('black'))
            Text3_surface = self.font.render(Text3,True,pygame.Color('black'))

            Text1_rect = Text1_surface.get_rect(topleft = Table.topleft)
            Text2_rect = Text2_surface.get_rect(midtop = Table.midtop)
            Text3_rect = ava.get_rect(topright = Table.topright)

            Surface.blit(Text1_surface,Text1_rect) 
            Surface.blit(Text2_surface,Text2_rect) 
            Surface.blit(ava, Text3_rect)

    DISPLAYSURF = screen
    BG =  pygame.image.load('Image/assets/Options/bg1.png').convert_alpha()
    BG = pygame.transform.scale(BG,(default_width*tyle,default_height*tyle))
    frame = pygame.image.load('Image/assets/Options/bg3.png')
    frame = pygame.transform.scale(frame, (1920*tyle,1080*tyle))
    information = Table_of_information(thongtin[0],thongtin[1],tyle)
    match_information = Table_of_match(thongtin[2],thongtin[3],thongtin[4])
    match_status = []

    L_arrow = pygame.image.load('Image/History/L-arrow.png').convert_alpha()
    R_arrow = pygame.image.load('Image/History/R-arrow.png').convert_alpha()
    Back_button = pygame.image.load('Image/History/back.png').convert_alpha()
    Back_button = pygame.transform.scale(Back_button,(300*tyle,150*tyle))

    L_arrow_rect = L_arrow.get_rect(midleft =(0*tyle,int(default_height/2*tyle)))
    R_arrow_rect = R_arrow.get_rect(midright =(1920*tyle,int(default_height/2*tyle)))
    Back_button_rect = Back_button.get_rect (bottomright = ((1920-45)* tyle,(1080-25)*tyle))

    start_point = 1

    if (len(thongtin[5]) < 5):
        for i in range (start_point,len(thongtin[5])):
            Temp_thongtin = [thongtin[5][i],thongtin[6][i],thongtin[7][i]]
            Temp = Table_of_match_status(Temp_thongtin,i,start_point,tyle)
            match_status.append(Temp)
        End = len(thongtin[5]) - start_point
    else:
        for i in range (start_point,start_point+4):
            Temp_thongtin = [thongtin[5][i],thongtin[6][i],thongtin[7][i]]
            Temp = Table_of_match_status(Temp_thongtin,i,start_point,tyle)
            match_status.append(Temp)
        End = 4

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if L_arrow_rect.collidepoint(mouse) :
                    if start_point > 1:
                        start_point -= 4

                        del match_status [:]    

                        for i in range (start_point,start_point+4):
                            Temp_thongtin = [thongtin[5][i],thongtin[6][i],thongtin[7][i]]
                            Temp = Table_of_match_status(Temp_thongtin,i,start_point,tyle)
                            match_status.append(Temp)
                        
                        End = 4    

                elif R_arrow_rect.collidepoint(mouse) :

                    if start_point + 4 < len(thongtin[5]):

                        start_point += 4

                        if (len(thongtin[5]) - 1 - start_point >=4 ):

                            del match_status [:]    

                            for i in range (start_point,start_point+4):
                                Temp_thongtin = [thongtin[5][i],thongtin[6][i],thongtin[7][i]]
                                Temp = Table_of_match_status(Temp_thongtin,i,start_point,tyle)
                                match_status.append(Temp)
                            End = 4
                        
                        else:
                            End = len(thongtin[5]) - start_point 

                            del match_status [:]    

                            for i in range (start_point,len(thongtin[5])):
                                Temp_thongtin = [thongtin[5][i],thongtin[6][i],thongtin[7][i]]
                                Temp = Table_of_match_status(Temp_thongtin,i,start_point,tyle)
                                match_status.append(Temp)
                
                elif Back_button_rect.collidepoint(mouse):
                    click_sound.play()
                    function.main_menu(screen, username, 0)

        DISPLAYSURF.blit(BG,(0,0))
        DISPLAYSURF.blit(frame, (0,0))
        DISPLAYSURF.blit(L_arrow,L_arrow_rect)
        DISPLAYSURF.blit(R_arrow,R_arrow_rect)
        DISPLAYSURF.blit(Back_button,Back_button_rect)
 
        information.draw(DISPLAYSURF,tyle)
        match_information.draw(DISPLAYSURF,tyle)

        for i in range (0,End): 
            match_status[i].draw(DISPLAYSURF,tyle)

        pygame.display.update()
# history(pygame.display.set_mode((1024,534)), "TungDo", 1024/1920, ioexcel.laythongtinhienthi("TungDo"))