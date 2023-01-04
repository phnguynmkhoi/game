import pygame
import sys
import function,user_account,newdraw,ioexcel
from pygame import mixer
import try_nam
pygame.init()

username = user_account.LoginRegister()

icon = pygame.image.load('banner/formula-1.png')
pygame.display.set_caption('CRAZIEST RACE')
pygame.display.set_icon(icon)

def main():
    global username
    if username !='':
        #Tao cua so game
        WIDTH = 1024
        HEIGHT = 534
        RESOLUTION = (WIDTH,HEIGHT)
        ioexcel.laythongtin(username)
        screen = pygame.display.set_mode(RESOLUTION)
        newdraw.fadein(screen)
        mixer.music.load('Music/bgm_menu.mp3')
        mixer.music.set_volume(0.2)
        mixer.music.play(-1,45,2000)
        function.main_menu(screen,username,0)
main()