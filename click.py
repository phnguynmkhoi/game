import pygame,sys
import function, ioexcel,try_nam
import main_minigame1 as mn1
import main_minigame2 as mn2
from pygame import mixer

pygame.init()

click_sound = mixer.Sound('Music/click.mp3')
#
chedo = 2
tiencuoc = 100
doan = 0
vitri = 1
namee =''
music_on = 1
giohang = ''
luotdau = ()
#

def main_menu(screen, username, selection):
    global namee, cart
    namee = username
    WIDTH, HEIGHT = screen.get_size()
    mouse = pygame.mouse.get_pos()
    Left = WIDTH*0.6
    Top = HEIGHT*0.2
    Bot = HEIGHT*0.9
    Width_1cell = WIDTH*0.28
    Height_1cell = (Bot-Top)/6

    # MENU OBJECT=========================================================================
    MENU_OBJECT = [
    pygame.Rect(Left, Top,                Width_1cell, Height_1cell),
    pygame.Rect(Left, Top+1*Height_1cell, Width_1cell, Height_1cell),
    pygame.Rect(Left, Top+2*Height_1cell, Width_1cell, Height_1cell),
    pygame.Rect(Left, Top+3*Height_1cell, Width_1cell, Height_1cell),
    pygame.Rect(Left, Top+4*Height_1cell, Width_1cell, Height_1cell)]
    
    if MENU_OBJECT[0].collidepoint(mouse):
        click_sound.play()
        function.choose_track(screen,username,0)
    if MENU_OBJECT[1].collidepoint(mouse):
        click_sound.play()
        function.history(screen, username)
    if MENU_OBJECT[2].collidepoint(mouse):
        click_sound.play()
        function.options(screen, username)
    if MENU_OBJECT[3].collidepoint(mouse):
        click_sound.play()
        cart = ioexcel.laymabua()
        function.help(screen, username, 0, 0)
    if MENU_OBJECT[4].collidepoint(mouse):
        click_sound.play()
        ioexcel.writeExcel()
        pygame.quit()
        sys.exit()

def options(screen, username):
    global music_on
    WIDTH, HEIGHT = screen.get_size()
    Width_1Cell = WIDTH*0.2
    Height_1Cell = WIDTH*0.04
    Range = WIDTH*0.015
    Left = WIDTH*0.18
    Top  = HEIGHT*0.35
    
    BUT_OBJ = [
    pygame.Rect(Left, Top, Width_1Cell, Height_1Cell),
    pygame.Rect(Left, Top+1*(Height_1Cell+Range), Width_1Cell, Height_1Cell),
    pygame.Rect(Left, Top+2*(Height_1Cell+Range), Width_1Cell, Height_1Cell),
    pygame.Rect(Left, Top+3*(Height_1Cell+Range), Width_1Cell, Height_1Cell),
    pygame.Rect(Left, Top+4*(Height_1Cell+Range), Width_1Cell, Height_1Cell)]
    
    mouse = pygame.mouse.get_pos()
    if BUT_OBJ[0].collidepoint(mouse):
        click_sound.play()
        screen = pygame.display.set_mode((960,540))
    if BUT_OBJ[1].collidepoint(mouse):
        click_sound.play()
        screen = pygame.display.set_mode((1280,720))
    if BUT_OBJ[2].collidepoint(mouse):
        click_sound.play()
        screen = pygame.display.set_mode((1600,900))
    if BUT_OBJ[3].collidepoint(mouse):
        click_sound.play()
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        WIDTH, HEIGHT = screen.get_size()
    if BUT_OBJ[4].collidepoint(mouse):
        click_sound.play()
        function.main_menu(screen, username, 0)
        
    SOUND_ON = pygame.Rect(WIDTH*0.7, Top, Width_1Cell, Height_1Cell)
    SOUND_OFF = pygame.Rect(WIDTH*0.7, Top+1*(Height_1Cell+Range), Width_1Cell, Height_1Cell)
    
    if SOUND_OFF.collidepoint(mouse):
        click_sound.play()
        mixer.music.set_volume(0)
    if SOUND_ON.collidepoint(mouse):
        click_sound.play()
        mixer.music.set_volume(0.2)

def help(screen, username, selection_help, goback):
    mouse = pygame.mouse.get_pos()
    WIDTH, HEIGHT = screen.get_size()
    Width_1cell = WIDTH*0.14
    Height_1cell = HEIGHT*0.08
    help_width = WIDTH*0.6
    help_height = HEIGHT*0.8
    Left = (WIDTH*0.5) - Width_1cell/2
    Top = HEIGHT*0.8
    
    # MINIGAME OBJECT
    HELP_OBJECT = [
    pygame.Rect(WIDTH*0.12, HEIGHT*0.45, Height_1cell, Height_1cell),
    pygame.Rect(WIDTH*0.88 - Height_1cell, HEIGHT*0.45, Height_1cell, Height_1cell),
    pygame.Rect(Left, Top, Width_1cell, Height_1cell)]
    
    if HELP_OBJECT[0].collidepoint(mouse):
        if selection_help >= 1:
            click_sound.play()
            function.help(screen, username, selection_help-1, goback)
    if HELP_OBJECT[1].collidepoint(mouse):
        if selection_help <= 9:
            click_sound.play()
            function.help(screen, username, selection_help+1, goback)
    if HELP_OBJECT[2].collidepoint(mouse):
        click_sound.play()
        if goback == 0:
            function.main_menu(screen, username, 0)
        if goback == 1:
            function.choose_track(screen, username,0)

def minigame1(screen, username):
    WIDTH, HEIGHT = screen.get_size()
    mouse = pygame.mouse.get_pos()

    Width_1cell = WIDTH*0.14
    Height_1cell = HEIGHT*0.08
    Left = (WIDTH*0.48) - Width_1cell
    Top = HEIGHT*0.87
    
    # MINIGAME OBJECT
    MNG_OBJECT = [
    pygame.Rect(Left,                            Top, Width_1cell, Height_1cell),
    pygame.Rect(Left + Width_1cell + 0.04*WIDTH, Top, Width_1cell, Height_1cell)]

    if MNG_OBJECT[0].collidepoint(mouse):
        click_sound.play()
        function.choose_minigame(screen, username, 0)
    if MNG_OBJECT[1].collidepoint(mouse):
        click_sound.play()
        mn1.minigame1(screen,username)

def minigame2(screen, username):
    WIDTH, HEIGHT = screen.get_size()
    mouse = pygame.mouse.get_pos()

    Width_1cell = WIDTH*0.14
    Height_1cell = HEIGHT*0.08
    Left = (WIDTH*0.48) - Width_1cell
    Top = HEIGHT*0.87
    
    # MINIGAME OBJECT
    MNG_OBJECT = [
    pygame.Rect(Left,                            Top, Width_1cell, Height_1cell),
    pygame.Rect(Left + Width_1cell + 0.04*WIDTH, Top, Width_1cell, Height_1cell)]

    if MNG_OBJECT[0].collidepoint(mouse):
        click_sound.play()
        function.choose_minigame(screen, username, 0)
    if MNG_OBJECT[1].collidepoint(mouse):
        click_sound.play()
        mn2.minigame2(screen,username)
        
def store(screen, username):
    global giohang
    mouse = pygame.mouse.get_pos()
    WIDTH, HEIGHT = screen.get_size()
    CENTER = WIDTH*0.5
    Width_1Cell = WIDTH*0.15
    Height_1Cell = WIDTH*0.225
    Range = WIDTH*0.015
    Left = WIDTH*0.18
    Top  = HEIGHT*0.15
    
    BACK_OBJ = pygame.Rect(20,20, WIDTH*0.18, HEIGHT*0.1)
    
    ITEM_OBJ = [
    pygame.Rect(CENTER - 2*Width_1Cell , HEIGHT*0.05,                    Width_1Cell, Height_1Cell*2/5),
    pygame.Rect(CENTER - 2*Width_1Cell , HEIGHT*0.05+Height_1Cell*3/5,   Width_1Cell, Height_1Cell*2/5),
    pygame.Rect(CENTER - 2*Width_1Cell , HEIGHT*0.05+2*Height_1Cell*3/5, Width_1Cell, Height_1Cell*2/5),
    pygame.Rect(CENTER - 2*Width_1Cell , HEIGHT*0.05+3*Height_1Cell*3/5, Width_1Cell, Height_1Cell*2/5)
    ]
    
    if BACK_OBJ.collidepoint(mouse):
        click_sound.play()
        function.choose_track(screen, username,0)
    
    giohang = ioexcel.laymabua()
    tongtien = ioexcel.layTongtien(username)
    if giohang == None:
        giohang = ''
    if len(giohang) < 9*2:
        if ITEM_OBJ[0].collidepoint(mouse) and tongtien>= 300: # Ten lua
            click_sound.play()
            giohang += ';1'
            ioexcel.tong_tien(username, -300)
        if ITEM_OBJ[1].collidepoint(mouse) and tongtien>= 100: # Mien khong
            click_sound.play()
            giohang += ';2'
            ioexcel.tong_tien(username, -100)
        if ITEM_OBJ[2].collidepoint(mouse) and tongtien>= 200: # Sach
            click_sound.play()
            giohang += ';3'
            ioexcel.tong_tien(username, -200)
        if ITEM_OBJ[3].collidepoint(mouse) and tongtien>= 200: # Hop bi an
            click_sound.play()
            giohang += ';4'
            ioexcel.tong_tien(username, -200)

    ioexcel.updatemabua(giohang)
    
def choose_minigame(screen, username, selection_mini):
    WIDTH, HEIGHT = screen.get_size()
    mouse = pygame.mouse.get_pos()
    # SET-BOARD LOCATION
    Width_1cell = WIDTH*0.16
    Height_1cell = HEIGHT*0.16
    Range_2cell = (HEIGHT*0.6-3*Height_1cell)/2
    Left = WIDTH*0.16
    Right = Left + Width_1cell
    Top = HEIGHT*0.3
    
    # MNG OBJECT BUTTON
    MNG_OBJECT = [
    pygame.Rect(Left,Top                                                           ,Width_1cell*1.5, Height_1cell*2),
    pygame.Rect(Left+2*(Width_1cell+Range_2cell),Top                                 ,Width_1cell*1.5,Height_1cell*2)
    ]

    # MINIGAME LIST====================================================================
    if MNG_OBJECT[0].collidepoint(mouse): 
        click_sound.play()
        function.choose_minigame(screen, username, 0)
    if MNG_OBJECT[1].collidepoint(mouse): 
        click_sound.play()
        function.choose_minigame(screen, username, 1)

    #========#
    Width_1cell = WIDTH*0.15
    Height_1cell = HEIGHT*0.08
    Range_2cell = HEIGHT*0.02
    Left = WIDTH*0.1
    Right = WIDTH*0.9
    Top = HEIGHT*0.75
    
    # MENU LOCATION
    MENU_LOCATION = [
    (Left,Top),
    (Right-Width_1cell*1.1,Top),
    #(Left,Top+(Height_1cell + Range_2cell))]
    ]
    
    # MENU OBJECT BUTTON
    MENU_OBJECT = [
    pygame.Rect(Left,Top                                          ,Width_1cell,Height_1cell),
    pygame.Rect(Right-Width_1cell,Top,                             Width_1cell,Height_1cell),
    #pygame.Rect(Left,             Top+(Height_1cell + Range_2cell),Width_1cell,Height_1cell)]
    ]
    score=0
    if MENU_OBJECT[1].collidepoint(mouse):
        click_sound.play()
        if selection_mini == 0:
            mn1.minigame1(screen,username)
        """  newdraw.minigame1(screen,username)
            minigame1(screen,username) """
        if selection_mini == 1:
            mn2.minigame2(screen,username)
        """  newdraw.minigame1(screen,username)
            minigame2(screen,username) """
    if MENU_OBJECT[0].collidepoint(mouse): 
        click_sound.play()
        function.choose_track(screen, username,0)

def choose_track(screen, username, selection_track):
    WIDTH, HEIGHT = screen.get_size()
    mouse = pygame.mouse.get_pos()
    # SET-BOARD LOCATION
    Width_1cell = WIDTH*0.16
    Height_1cell = HEIGHT*0.16
    Range_2cell = (HEIGHT*0.6-3*Height_1cell)/2
    Left = WIDTH*0.16
    Right = Left + Width_1cell
    Top = HEIGHT*0.1
    
    cart = ioexcel.laymabua()
    Store = pygame.Rect(0,0, WIDTH*0.07,WIDTH*0.07)
    
    if Store.collidepoint(mouse):
        click_sound.play()
        function.store(screen, username, cart)
    
    # MAP OBJECT BUTTON
    MAP_OBJECT = [
    pygame.Rect(Left,Top                                                           ,Width_1cell,Height_1cell),
    pygame.Rect(Left+Width_1cell+2*Range_2cell,Top                                 ,Width_1cell,Height_1cell),
    pygame.Rect(Left+2*(Width_1cell+2*Range_2cell),Top                             ,Width_1cell,Height_1cell),
    pygame.Rect(Left+Width_1cell/2,Top+1*(Height_1cell + 2*Range_2cell)            ,Width_1cell,Height_1cell),
    pygame.Rect(Left+2*Width_1cell+Range_2cell,Top+1*(Height_1cell + 2*Range_2cell),Width_1cell,Height_1cell)
    ]
    
    # MAP LIST====================================================================

    if MAP_OBJECT[0].collidepoint(mouse): 
        click_sound.play()
        function.choose_track(screen, username, 0)
    if MAP_OBJECT[1].collidepoint(mouse): 
        click_sound.play()
        function.choose_track(screen, username, 1)
    if MAP_OBJECT[2].collidepoint(mouse): 
        click_sound.play()
        function.choose_track(screen, username, 2)
    if MAP_OBJECT[3].collidepoint(mouse): 
        click_sound.play()
        function.choose_track(screen, username, 3)
    if MAP_OBJECT[4].collidepoint(mouse): 
        click_sound.play()
        function.choose_track(screen, username, 4)

    #========#
    Width_1cell = WIDTH*0.2
    Height_1cell = HEIGHT*0.06
    Range_2cell = HEIGHT*0.02
    Left = WIDTH*0.1
    Right = WIDTH*0.9
    Top = HEIGHT*0.77
    
    # MENU LOCATION
    MENU_LOCATION = [
    (Left,Top),
    (Right-Width_1cell,Top),
    (Left,Top+(Height_1cell + Range_2cell)),
    (Right-Width_1cell,Top+(Height_1cell + Range_2cell))]
    
    # MENU OBJECT BUTTON
    MENU_OBJECT = [
    pygame.Rect(Left,Top                                          ,Width_1cell,Height_1cell),
    pygame.Rect(Right-Width_1cell,Top,                             Width_1cell,2*Height_1cell),
    pygame.Rect(Left,             Top+(Height_1cell + Range_2cell),Width_1cell,Height_1cell)]
    if selection_track >=0 and selection_track <=4:
        if MENU_OBJECT[1].collidepoint(mouse):
            if ioexcel.layTongtien(username) >= 100:
                click_sound.play()
                function.choose_set(screen,username,selection_track,0,0)
            else :
                click_sound.play()
                function.choose_minigame(screen,username,1) #else thì vô minigame
    if MENU_OBJECT[0].collidepoint(mouse): 
        click_sound.play()
        function.main_menu(screen, username, 0)
    if MENU_OBJECT[2].collidepoint(mouse): 
        click_sound.play()
        function.help(screen, username, 0, 1)
        
def choose_set(screen, username, selection_track, selection_set,selection_char):
    WIDTH, HEIGHT = screen.get_size()
    mouse = pygame.mouse.get_pos()
    # SET-BOARD LOCATION
    bg_choose_WIDTH = WIDTH*0.6
    bg_choose_HEIGHT = HEIGHT*0.6
    Width_1cell = bg_choose_WIDTH*0.78
    Height_1cell = bg_choose_HEIGHT*0.2
    Range_2cell = (bg_choose_HEIGHT-5*Height_1cell)/6
    Left = bg_choose_WIDTH*0.1 + WIDTH*0.06
    Right = Left + Width_1cell
    Top = HEIGHT*0.08
    
    cart = ioexcel.laymabua()
    Store = pygame.Rect(0,0, WIDTH*0.07,WIDTH*0.07)
    
    if Store.collidepoint(mouse):
        click_sound.play()
        function.store(screen, username, cart)
    
    # SET OBJECT BUTTON
    SET_OBJECT = [
    pygame.Rect(Left,Top                               ,Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+1*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+2*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+3*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+4*(Height_1cell + Range_2cell),Width_1cell,Height_1cell)]
    # SET LIST====================================================================

    if SET_OBJECT[0].collidepoint(mouse): 
        click_sound.play()
        function.choose_set(screen, username,selection_track, 0, selection_char)
    if SET_OBJECT[1].collidepoint(mouse): 
        click_sound.play()
        function.choose_set(screen, username,selection_track, 1, selection_char)
    if SET_OBJECT[2].collidepoint(mouse): 
        click_sound.play()
        function.choose_set(screen, username,selection_track, 2, selection_char)
    if SET_OBJECT[3].collidepoint(mouse): 
        click_sound.play()
        function.choose_set(screen, username,selection_track, 3, selection_char)
    if SET_OBJECT[4].collidepoint(mouse): 
        click_sound.play()
        function.choose_set(screen, username,selection_track, 4, selection_char)
    
    Width_1cell = WIDTH*0.12
    Height_1cell = HEIGHT*0.1
    Range_2cell = (HEIGHT*0.6-5*Height_1cell)/5
    Left = WIDTH*0.78
    Top = HEIGHT*0.08
    
    # CHAR OBJECT BUTTON
    CHA_OBJECT = [
    pygame.Rect(Left,Top                               ,Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+1*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+2*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+3*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+4*(Height_1cell + Range_2cell),Width_1cell,Height_1cell)]
    
    if CHA_OBJECT[0].collidepoint(mouse): 
        click_sound.play()
        function.choose_set(screen, username, selection_track,selection_set, 0)
    if CHA_OBJECT[1].collidepoint(mouse): 
        click_sound.play()
        function.choose_set(screen, username, selection_track, selection_set, 1)
    if CHA_OBJECT[2].collidepoint(mouse): 
        click_sound.play()
        function.choose_set(screen, username, selection_track, selection_set, 2)
    if CHA_OBJECT[3].collidepoint(mouse): 
        click_sound.play()
        function.choose_set(screen, username, selection_track, selection_set, 3)
    if CHA_OBJECT[4].collidepoint(mouse): 
        click_sound.play()
        function.choose_set(screen, username, selection_track, selection_set, 4)
    
    Width_1cell = WIDTH*0.2
    Height_1cell = HEIGHT*0.06
    Range_2cell = HEIGHT*0.02
    Left = WIDTH*0.1
    Right = WIDTH*0.9
    Top = HEIGHT*0.77
    
    # MENU LOCATION
    MENU_LOCATION = [
    (Left,Top),
    (Right-Width_1cell,Top),
    (Left,Top+(Height_1cell + Range_2cell)),
    (Right-Width_1cell,Top+(Height_1cell + Range_2cell))]
    
    # MENU OBJECT BUTTON
    MENU_OBJECT = [
    pygame.Rect(Left,Top                                          ,Width_1cell,Height_1cell),
    pygame.Rect(Right-Width_1cell,Top,                             Width_1cell,2*Height_1cell),
    pygame.Rect(Left,             Top+(Height_1cell + Range_2cell),Width_1cell,Height_1cell)]
    
    if selection_set != -1 and selection_char != -1:
        if MENU_OBJECT[1].collidepoint(mouse):
            click_sound.play()
            function.choose_bet(screen, username,selection_track, selection_set*10 + selection_char, '', 1, 0 , 0)
        '''
            else:
                click_sound.play()
                function.choose_track(screen, username,selection_track, 1)
                #choose_minigame(screen, username,0)
        '''
    if MENU_OBJECT[0].collidepoint(mouse): 
        click_sound.play()
        function.choose_track(screen, username, 0)
    if MENU_OBJECT[2].collidepoint(mouse): 
        click_sound.play()
        function.help(screen, username, 0, 1)

def tongket(rank, manvcuoc, tongtien, tiencuoc):
    global luotdau
    tiengiaodong = 0
    checkwin = 0
    checkdoan = 0
    #if manvcuoc == rank[0][0]:
    if rank == 1:
        tiengiaodong += tiencuoc
        checkwin = 1
    else:
        tiengiaodong -= tiencuoc
    luotdau = (checkwin, tiengiaodong, manvcuoc)
    tongtien += tiengiaodong
    thongtin = tuple(str(rank)) + (checkwin, checkdoan, tongtien, tiengiaodong)
    
    return thongtin


def bet(screen, username,selection_track,set_char, char_name, rename, cost, mode):
    global chedo, tiencuoc, vitri
    WIDTH, HEIGHT = screen.get_size()
    mouse = pygame.mouse.get_pos()
    
    BACK_BUTTON = pygame.Rect(WIDTH*0.08,HEIGHT*0.85, WIDTH*0.12, HEIGHT*0.07)
    if BACK_BUTTON.collidepoint(mouse):
        #function.choose_set(screen, username,selection_track, set_char, char_name)
        function.choose_set(screen, username,selection_track, set_char/10, set_char%10)
    # CHAR OBJECT BUTTON
    CHA_OBJECT = pygame.Rect(WIDTH*0.13,  HEIGHT*0.15,WIDTH*0.3,  HEIGHT*0.55)
    
    BET_OBJECT = [
    pygame.Rect(WIDTH*0.55,  HEIGHT*0.15                ,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.55,  HEIGHT*0.15 + 1*HEIGHT*0.1 + HEIGHT*0.03  ,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.55,  HEIGHT*0.15 + 2*HEIGHT*0.1 + HEIGHT*0.03*2,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.74, HEIGHT*0.15                  ,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.74, HEIGHT*0.15 + 1*HEIGHT*0.1 + HEIGHT*0.03,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.74, HEIGHT*0.15 + 2*HEIGHT*0.1 + HEIGHT*0.03*2,WIDTH*0.15, HEIGHT*0.1)]
    
    if BET_OBJECT[0].collidepoint(mouse):
        click_sound.play()
        tiencuoc = 100
    if BET_OBJECT[1].collidepoint(mouse):
        if ioexcel.layTongtien(username) >= 500:
            click_sound.play()
            tiencuoc = 500
    if BET_OBJECT[2].collidepoint(mouse):
        click_sound.play()
        tiencuoc = ioexcel.layTongtien(username)/2
    if BET_OBJECT[3].collidepoint(mouse):
        if ioexcel.layTongtien(username) >= 200:
            click_sound.play()
            tiencuoc = 200
    if BET_OBJECT[4].collidepoint(mouse):
        if ioexcel.layTongtien(username) >= 1000:
            click_sound.play()
            tiencuoc = 1000
    if BET_OBJECT[5].collidepoint(mouse):
        click_sound.play()
        tiencuoc = ioexcel.layTongtien(username)
    if tiencuoc > ioexcel.layTongtien(username):
        tiencuoc = 100
        
    # MODe OBJECT BUTTON
    MODE_OBJECT = [
    pygame.Rect(WIDTH*0.55, HEIGHT*0.3 + 3*HEIGHT*0.1,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.67, HEIGHT*0.3 + 3*HEIGHT*0.1,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.79, HEIGHT*0.3 + 3*HEIGHT*0.1,WIDTH*0.15, HEIGHT*0.1)]
    
    if MODE_OBJECT[0].collidepoint(mouse):
        click_sound.play()
        chedo = 2
    if MODE_OBJECT[1].collidepoint(mouse):
        click_sound.play()
        chedo = 3
    if MODE_OBJECT[2].collidepoint(mouse):
        click_sound.play()
        chedo = 4
        
    TEXT_OBJECT1 = pygame.Rect(WIDTH*0.13,  HEIGHT*0.15, WIDTH*0.3, HEIGHT*0.05)
    if TEXT_OBJECT1.collidepoint(mouse): 
        click_sound.play()
        function.choose_bet(screen, username, selection_track, set_char, char_name, 1, cost, mode)
        
    START_OBJECT = pygame.Rect(5*WIDTH*0.13 + 100,HEIGHT*0.71,WIDTH*0.15, HEIGHT*0.15)

    if START_OBJECT.collidepoint(mouse):
        if ioexcel.layTongtien(username) >= tiencuoc:
            click_sound.play()
            #maingameplay.gameplaymain(screen,selection_track,username, str(set_char),char_name, tiencuoc, WIDTH/1920, chedo)
            #maingameplay.gameplaymain(screen, username,selection_track, set_char,char_name, tiencuoc, WIDTH/1920, chedo)
            tongtien = ioexcel.layTongtien(username)
            print(set_char)
            print(set_char%10)
            rank = try_nam.play(screen,selection_track,int(set_char/10),set_char%10,chedo,username,char_name)
            print(rank)
            thongtin = tongket(rank,set_char,tongtien,tiencuoc)
            ioexcel.writefile(username, luotdau)
            function.score(screen, username, thongtin,char_name,set_char,screen.get_size())

def score(screen, username, thongtin,tennv,nvcuoc,tile):
    mouse = pygame.mouse.get_pos()
    BACK = pygame.Rect((1920-20)*tile, (1080-20)*tile, 400*tile, 100*tile)
    if BACK.collidepoint(mouse):
        function.choose_set(screen, username,0, 0, 0)
        
def chuyenthongtin():
    return [tiencuoc, chedo, vitri, namee]