import pygame,sys,ioexcel
import random,click,ioexcel
pygame.init()

#screen = pygame.display.set_mode((1152,645)
tien = 0

def fadein(screen):
    WIDTH,HEIGHT = screen.get_size()
    fadein = pygame.Surface((WIDTH,HEIGHT))
    fadein.fill((225,225,225))
    for alpha in range (50,300,5):
        fadein.set_alpha(300-alpha)
        screen.blit(fadein,(0,0))
        pygame.display.update()
        logo = pygame.image.load('assets/background-menus-main.png').convert()
        logo = pygame.transform.scale(logo,(WIDTH,HEIGHT))
        screen.blit(logo,(0,0))
    pygame.time.delay(1500)

def fadeout(screen): 
    WIDTH, HEIGHT = screen.get_size()
    fadein = pygame.Surface((WIDTH,HEIGHT))
    fadein.fill((225,225,225))
    for alpha in range(0, 300):
        fadein.set_alpha(alpha)
        screen.blit(fadein, (0,0))
        pygame.display.update()
        logo = pygame.image.load('assets/background-menus-main.png').convert()
        screen.blit(logo, (0,0))
    pygame.time.delay(4)

def money(screen, username):
    WIDTH, HEIGHT = screen.get_size()
    money_int = ioexcel.layTongtien(username)
    font = pygame.font.Font('Font/Gamefont.ttf', int(WIDTH*0.024))
    money = font.render('Money: ' + str(money_int),True,(255,255,255))
    screen.blit(money, (WIDTH*0.78, 2))
    global tien
    tien = money_int

def store(screen, username, cart):
    WIDTH, HEIGHT = screen.get_size()
    CENTER = WIDTH*0.5
    Width_1Cell = WIDTH*0.15
    Height_1Cell = WIDTH*0.225
    Range = WIDTH*0.015
    Left = WIDTH*0.18
    Top  = HEIGHT*0.15
    
    bg = pygame.image.load('Image/Store/garage1.png')
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
    
    back = pygame.image.load('Image/assets/SetMenu/Back.png')
    back = pygame.transform.scale(back, (WIDTH*0.15, HEIGHT*0.1))

    item1 = pygame.image.load('Image/store/items/1.png')
    item2 = pygame.image.load('Image/store/items/2.png')
    item3 = pygame.image.load('Image/store/items/3.png')
    item4 = pygame.image.load('Image/store/items/4.png')
    
    item01 = pygame.image.load('Image/store/items/1-hover.png')
    item02 = pygame.image.load('Image/store/items/2-hover.png')
    item03 = pygame.image.load('Image/store/items/3-hover.png')
    item04 = pygame.image.load('Image/store/items/4-hover.png')

    saler1 = pygame.image.load('Image/store/saler1.png')
    saler2 = pygame.image.load('Image/store/saler2.png')
    saler3 = pygame.image.load('Image/store/saler3.png')
    saler4 = pygame.image.load('Image/store/saler4.png')

    ITEM_IMG = [
    pygame.transform.scale(item1, (Width_1Cell, Height_1Cell*2/5)),
    pygame.transform.scale(item2, (Width_1Cell, Height_1Cell*2/5)),
    pygame.transform.scale(item3, (Width_1Cell, Height_1Cell*2/5)),
    pygame.transform.scale(item4, (Width_1Cell, Height_1Cell*2/5)),
    ]
    
    ITEM_CLICK =[
    pygame.transform.scale(item01, (Width_1Cell, Height_1Cell*2/5)),
    pygame.transform.scale(item02, (Width_1Cell, Height_1Cell*2/5)),
    pygame.transform.scale(item03, (Width_1Cell, Height_1Cell*2/5)),
    pygame.transform.scale(item04, (Width_1Cell, Height_1Cell*2/5)),
    ]

    SALER_IMG = [
    pygame.transform.scale(saler1, (Width_1Cell*3/2, Height_1Cell*3/2)),
    pygame.transform.scale(saler2, (Width_1Cell*3/2, Height_1Cell*3/2)),
    pygame.transform.scale(saler3, (Width_1Cell*3/2, Height_1Cell*3/2)),
    pygame.transform.scale(saler4, (Width_1Cell*3/2, Height_1Cell*3/2)),
    ]

    ITEM_LOC = [
    (CENTER - 2*Width_1Cell , HEIGHT*0.05),
    (CENTER - 2*Width_1Cell , HEIGHT*0.05+Height_1Cell*3/5),
    (CENTER - 2*Width_1Cell , HEIGHT*0.05+2*Height_1Cell*3/5),
    (CENTER - 2*Width_1Cell , HEIGHT*0.05+3*Height_1Cell*3/5),]
    #vị trí seller
    saler_loc = (CENTER + Width_1Cell*3/2 , HEIGHT*0.3)

    ITEM_OBJ = [
    pygame.Rect(CENTER - 2*Width_1Cell , HEIGHT*0.05,                    Width_1Cell, Height_1Cell*2/5),
    pygame.Rect(CENTER - 2*Width_1Cell , HEIGHT*0.05+Height_1Cell*3/5,   Width_1Cell, Height_1Cell*2/5),
    pygame.Rect(CENTER - 2*Width_1Cell , HEIGHT*0.05+2*Height_1Cell*3/5, Width_1Cell, Height_1Cell*2/5),
    pygame.Rect(CENTER - 2*Width_1Cell , HEIGHT*0.05+3*Height_1Cell*3/5, Width_1Cell, Height_1Cell*2/5)
    ]

    font = pygame.font.Font('Font/Gamefont.ttf', int(WIDTH*0.024))
    font2 = pygame.font.Font('Font/Gamefont.ttf', int(WIDTH*0.018))
    NAME_ITEMS = [
    font.render('Buff Speed',True,(205,105,105),),
    font.render('Buff Effect',True,(205,105,105)),
    font.render('Remove Control',True,(205,105,105)),
    font.render('Mistery Box',True,(205,105,105))]
    '''
    MSG_ITEMS = [
        font2.render('Hang tough!',True,(35, 140, 0)),
        font2.render('Wise choice guy!',True,(35, 140, 0)),
        font2.render('Anything else?',True,(35, 140, 0)),
        font2.render('Thank you!',True,(35, 140, 0)),
    ]
    '''
    messages_list = ['Hang tough!','Wise choice guy!','Anything else?','Thank you!','Good luck!','I believe u!','Go get the money!']
    message = font2.render(random.choice(messages_list),True,(35, 140, 0))

    Left = WIDTH*0.02
    Top = HEIGHT*0.5
    # tạo khung msg
    msg = pygame.image.load('Image/Store/chat_box.png')
    msg = pygame.transform.scale(msg, (Width_1Cell*5/4, Height_1Cell))

    screen.blit(bg, (0, 0))
    screen.blit(back, (20,20))
    mouse = pygame.mouse.get_pos()
    
    for i in range(0, len(ITEM_OBJ)):
        if ITEM_OBJ[i].collidepoint(mouse):
            screen.blit(ITEM_CLICK[i], ITEM_LOC[i])
            screen.blit(NAME_ITEMS[i], (ITEM_LOC[i][0]+Width_1Cell, ITEM_LOC[i][1]+Height_1Cell/6))
            screen.blit(SALER_IMG[i],saler_loc)
            screen.blit(msg,(ITEM_LOC[0][0]+Width_1Cell*2, ITEM_LOC[0][1] + Height_1Cell*0.3))
            #screen.blit(MSG_ITEMS[i],(ITEM_LOC[0][0]+505, ITEM_LOC[0][1] + Height_1Cell*0.8-100))
            screen.blit(message,(ITEM_LOC[0][0]+Width_1Cell*11/5, ITEM_LOC[0][1] + Height_1Cell*0.5))
            pygame.time.wait(200)
        else:
            screen.blit(ITEM_IMG[i], ITEM_LOC[i])
            screen.blit(NAME_ITEMS[i], (ITEM_LOC[i][0]+Width_1Cell, ITEM_LOC[i][1]+Height_1Cell/6))
            #screen.blit(saler0,(ITEM_LOC[i][0]+470, ITEM_LOC[i][1] + Height_1Cell*0.8-170))
    #giỏ hàng
    if cart != None:
        for i in range(0, int(len(cart)/2)):
            if Top>=(HEIGHT-WIDTH*0.08):
                Top = HEIGHT*0.5
                Left += WIDTH*0.08
            cart_item = pygame.image.load('Image/Store/eff/' + cart[2*i+1] + '.png')
            cart_item = pygame.transform.scale(cart_item, (HEIGHT/10, HEIGHT/10))
            if cart[2*i+1] != 0:
                screen.blit(cart_item, (Left,Top))
                Top += WIDTH*0.08

def choose_minigame (screen,username,selection_mini):
    WIDTH, HEIGHT = screen.get_size()
    # image
    background = pygame.image.load('Image/choose mini/choose mini.png').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    screen.blit(background, (0,0))

    # MINIGAME-BOARD LOCATION
    Width_1cell = WIDTH*0.16
    Height_1cell = HEIGHT*0.16
    Range_2cell = (HEIGHT*0.6-3*Height_1cell)/2
    Left = WIDTH*0.16
    Right = Left + Width_1cell
    Top = HEIGHT*0.3

    # LOAD IMAGE
    minigame_1_img = pygame.image.load('Image/choose mini/minigame1.png')
    minigame_2_img = pygame.image.load('Image/choose mini/minigame2.png')
    minigame_01_img = pygame.image.load('Image/choose mini/minigame1-hover.png')
    minigame_02_img = pygame.image.load('Image/choose mini/minigame2-hover.png')
    # MINIGAME IMAGE
    minigame_img = [ 
    pygame.transform.scale(minigame_1_img, (Width_1cell*1.5, Height_1cell*2)),
    pygame.transform.scale(minigame_2_img, (Width_1cell*1.5, Height_1cell*2)),
    ]
    minigame_click =[
    pygame.transform.scale(minigame_01_img, (Width_1cell*1.5, Height_1cell*2)),
    pygame.transform.scale(minigame_02_img, (Width_1cell*1.5, Height_1cell*2)),
    ]
    
    # MINIGAME OBJECT BUTTON
    MNG_OBJECT = [
    pygame.Rect(Left,Top                                                           ,Width_1cell*1.5, Height_1cell*2),
    pygame.Rect(Left+2*(Width_1cell+Range_2cell),Top                                 ,Width_1cell*1.5,Height_1cell*2)]
    
    # MINIGAME LOCATION
    MNG_LOCATION = [
    (Left,Top),
    (Left+2*(Width_1cell+Range_2cell),Top)
    ]
    
    # MOUSE LOCATION
    mouse = pygame.mouse.get_pos()
    # SET LIST===========================================================================
    
    for i in range(0, len(MNG_OBJECT)):
        if  selection_mini == i:
            screen.blit(minigame_click[i], (MNG_LOCATION[i][0],MNG_LOCATION[i][1]-10))
            #screen.blit(set_img[5], SET_LOCATION[i])
            #screen.blit(arrow, (WIDTH*0.62, Top))
        else:
            screen.blit(minigame_img[i], MNG_LOCATION[i])
        Top += Height_1cell + Range_2cell
    # ====================================================================================
    
    # MENU-BOARD LOCATION
    Width_1cell = WIDTH*0.15
    Height_1cell = HEIGHT*0.08
    Range_2cell = HEIGHT*0.02
    Left = WIDTH*0.1
    Right = WIDTH*0.9
    Top = HEIGHT*0.75
    # Truoc khi click
    Back = pygame.image.load('img/background-menus/buttons/7.png')
    Play = pygame.image.load('img/background-menus/buttons/1.png')
    # Sau khi click
    Back1 = pygame.image.load('img/background-menus/buttons/07.png')
    Play1 = pygame.image.load('img/background-menus/buttons/01.png')

    MENU_IMG = [
    pygame.transform.scale(Back, (Width_1cell, Height_1cell)),
    pygame.transform.scale(Play, (Width_1cell, Height_1cell)),
    #pygame.transform.scale(Help, (1.2*Width_1cell, 1.8*Height_1cell)),
    ]

    MENU_CLICK = [
    pygame.transform.scale(Back1, (Width_1cell, Height_1cell)),
    pygame.transform.scale(Play1, (Width_1cell, Height_1cell)),
    #pygame.transform.scale(Help1, (1.2*Width_1cell, 1.8*Height_1cell))]
    ]
    # MENU LOCATION
    MENU_LOCATION = [
    (Left,Top),
    (Right-Width_1cell*1.1,Top),
    #(Left,Top+(Height_1cell + Range_2cell))]
    ]
    
    # MENU OBJECT BUTTON
    MENU_OBJECT = [
    pygame.Rect(Left,Top  ,Width_1cell,Height_1cell),
    pygame.Rect(Right-Width_1cell,Top,  Width_1cell,Height_1cell),
    ]
    for i in range(0, len(MENU_OBJECT)):
        if MENU_OBJECT[i].collidepoint(mouse):
            screen.blit(MENU_CLICK[i], MENU_LOCATION[i])
        else:
            screen.blit(MENU_IMG[i], MENU_LOCATION[i])

def choose_track(screen,username,selection_track):
    WIDTH, HEIGHT = screen.get_size()
    # image
    background = pygame.image.load('Image/choose track/choose_track.png').convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    Store = pygame.image.load('Image/Store/store_ico.png')
    Store = pygame.transform.scale(Store, (WIDTH*0.07,WIDTH*0.07))

    screen.blit(background, (0,0))
    screen.blit(Store, (0,0))

    # TRACK-BOARD LOCATION
    Width_1cell = WIDTH*0.16
    Height_1cell = HEIGHT*0.16
    Range_2cell = (HEIGHT*0.6-3*Height_1cell)/2
    Left = WIDTH*0.16
    Right = Left + Width_1cell
    Top = HEIGHT*0.1

    # LOAD IMAGE
    #hover = pygame.image.load()
    track_1_img = pygame.image.load('img/background-levels/background-city-0.png')
    track_2_img = pygame.image.load('img/background-levels/background-desert-0.png')
    track_3_img = pygame.image.load('img/background-levels/background-galaxy-0.png')
    track_4_img = pygame.image.load('img/background-levels/background-painting-0.png')
    track_5_img = pygame.image.load('img/background-levels/background-sea-0.png')
    track_1_img_c = pygame.image.load('img/background-levels/background-city-0-c.png')
    track_2_img_c = pygame.image.load('img/background-levels/background-desert-0-c.png')
    track_3_img_c = pygame.image.load('img/background-levels/background-galaxy-0-c.png')
    track_4_img_c = pygame.image.load('img/background-levels/background-painting-0-c.png')
    track_5_img_c = pygame.image.load('img/background-levels/background-sea-0-c.png')
    
    # TRACK IMAGE
    track_img = [ 
    pygame.transform.scale(track_1_img, (Width_1cell, Height_1cell)),
    pygame.transform.scale(track_2_img, (Width_1cell, Height_1cell)),
    pygame.transform.scale(track_3_img, (Width_1cell, Height_1cell)),
    pygame.transform.scale(track_4_img, (Width_1cell, Height_1cell)),
    pygame.transform.scale(track_5_img, (Width_1cell, Height_1cell)),
    ]
    track_img_c=[
    pygame.transform.scale(track_1_img_c, (Width_1cell, Height_1cell)),
    pygame.transform.scale(track_2_img_c, (Width_1cell, Height_1cell)),
    pygame.transform.scale(track_3_img_c, (Width_1cell, Height_1cell)),
    pygame.transform.scale(track_4_img_c, (Width_1cell, Height_1cell)),
    pygame.transform.scale(track_5_img_c, (Width_1cell, Height_1cell)),
    ]
    # TRACK OBJECT BUTTON
    TRACK_OBJECT = [
    pygame.Rect(Left,Top                                                           ,Width_1cell,Height_1cell),
    pygame.Rect(Left+Width_1cell+2*Range_2cell,Top                                 ,Width_1cell,Height_1cell),
    pygame.Rect(Left+2*(Width_1cell+2*Range_2cell),Top                             ,Width_1cell,Height_1cell),
    pygame.Rect(Left+Width_1cell/2,Top+1*(Height_1cell + 2*Range_2cell)            ,Width_1cell,Height_1cell),
    pygame.Rect(Left+2*Width_1cell+Range_2cell,Top+1*(Height_1cell + 2*Range_2cell),Width_1cell,Height_1cell)]
    
    # TRACK LOCATION
    TRACK_LOCATION = [
    (Left,Top),
    (Left+Width_1cell+2*Range_2cell,Top),
    (Left+2*(Width_1cell+2*Range_2cell),Top),
    (Left+Width_1cell/2,Top+1*(Height_1cell + 2*Range_2cell)),
    (Left+2*Width_1cell+Range_2cell,Top+1*(Height_1cell + 2*Range_2cell))
    ]
    
    # MOUSE LOCATION
    mouse = pygame.mouse.get_pos()
    # TRACK LIST===========================================================================
    
    for i in range(0, len(TRACK_OBJECT)):
        if  selection_track == i:
            screen.blit(track_img_c[i], (TRACK_LOCATION[i][0],TRACK_LOCATION[i][1]-10))
            #screen.blit(set_img[5], SET_LOCATION[i])
            #screen.blit(arrow, (WIDTH*0.62, Top))
        else:
            screen.blit(track_img[i], TRACK_LOCATION[i])
        Top += Height_1cell + Range_2cell
    # ====================================================================================
    
    # MENU-BOARD LOCATION
    Width_1cell = WIDTH*0.15
    Height_1cell = HEIGHT*0.08
    Range_2cell = HEIGHT*0.02
    Left = WIDTH*0.1
    Right = WIDTH*0.9
    Top = HEIGHT*0.75
    
    Back = pygame.image.load('Image/assets/SetMenu/back.png')
    Help = pygame.image.load('Image/assets/SetMenu/help.png')
    Next = pygame.image.load('Image/assets/SetMenu/next.png')

    MENU_IMG = [
    pygame.transform.scale(Back, (Width_1cell, Height_1cell)),
    pygame.transform.scale(Next, (1.2*Width_1cell, 1.8*Height_1cell)),
    pygame.transform.scale(Help, (Width_1cell, Height_1cell))]
    
    # MENU LOCATION
    MENU_LOCATION = [
    (Left,Top),
    (Right-Width_1cell*1.1,Top),
    (Left,Top+(Height_1cell + Range_2cell))]
    
    # MENU OBJECT BUTTON
    MENU_OBJECT = [
    pygame.Rect(Left,Top  ,Width_1cell,Height_1cell),
    pygame.Rect(Right-Width_1cell,Top,  Width_1cell,Height_1cell),
    pygame.Rect(Left, Top+(Height_1cell + Range_2cell),Width_1cell,Height_1cell)]
    
    for i in range(0, len(MENU_OBJECT)):
        if MENU_OBJECT[i].collidepoint(mouse):
            screen.blit(MENU_IMG[i], MENU_LOCATION[i])
        else:
            screen.blit(MENU_IMG[i], MENU_LOCATION[i])

def choose_set(screen, username, selection_set,selection_char,selection_track):
    WIDTH, HEIGHT = screen.get_size()
    # image
    background=[]
    for i in range(5):
        img=f"Image/choose set/bg{i}.png"
        img=pygame.image.load(img)
        img=pygame.transform.scale(img, (WIDTH, HEIGHT))
        background.append(img)
    # background = pygame.image.load('Image/choose set/choose_set.png').convert()
    # background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    Store = pygame.image.load('Image/Store/store_ico.png')
    Store = pygame.transform.scale(Store, (WIDTH*0.07,WIDTH*0.07))
    
    screen.blit(background[selection_track], (0,0))
    screen.blit(Store, (0,0))
    
    # SET-BOARD LOCATION
    Width_1cell = WIDTH*0.47
    Height_1cell = HEIGHT*0.12
    Range_2cell = (HEIGHT*0.6-5*Height_1cell)/6
    Left = WIDTH*0.12
    Right = Left + Width_1cell
    Top = HEIGHT*0.08
    
    # LOAD IMAGE
    arrow = pygame.image.load('Image/assets/SetMenu/arrow.png')
    arrow = pygame.transform.scale(arrow, (Height_1cell, Height_1cell))
    set_0_img = pygame.image.load('Image/Characters/ava/0.png')
    set_1_img = pygame.image.load('Image/Characters/set1.png')
    set_2_img = pygame.image.load('Image/Characters/set2.png')
    set_3_img = pygame.image.load('Image/Characters/set3.png')
    set_4_img = pygame.image.load('Image/Characters/set4.png')
    set_5_img = pygame.image.load('Image/Characters/set5.png')
    
    # SET IMAGE
    set_img = [ 
    pygame.transform.scale(set_1_img, (Width_1cell, Height_1cell)),
    pygame.transform.scale(set_2_img, (Width_1cell, Height_1cell)),
    pygame.transform.scale(set_3_img, (Width_1cell, Height_1cell)),
    pygame.transform.scale(set_4_img, (Width_1cell, Height_1cell)),
    pygame.transform.scale(set_5_img, (Width_1cell, Height_1cell)),
    pygame.transform.scale(set_0_img, (Width_1cell, Height_1cell))]
    
    # SET OBJECT BUTTON
    SET_OBJECT = [
    pygame.Rect(Left,Top                               ,Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+1*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+2*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+3*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+4*(Height_1cell + Range_2cell),Width_1cell,Height_1cell)]
    
    # SET LOCATION
    SET_LOCATION = [
    (Left,Top),
    (Left,Top+1*(Height_1cell + Range_2cell)),
    (Left,Top+2*(Height_1cell + Range_2cell)),
    (Left,Top+3*(Height_1cell + Range_2cell)),
    (Left,Top+4*(Height_1cell + Range_2cell))]
    
    # MOUSE LOCATION
    mouse = pygame.mouse.get_pos()
    # SET LIST===========================================================================
    for i in range(0, len(SET_OBJECT)):
        if  selection_set == i:
            screen.blit(set_img[i], SET_LOCATION[i])
            # screen.blit(set_img[5], SET_LOCATION[i])
            screen.blit(arrow, (WIDTH*0.62, Top))
        else:
            screen.blit(set_img[i], SET_LOCATION[i])
        Top += Height_1cell + Range_2cell
    # ====================================================================================
    
    # MENU-BOARD LOCATION
    Width_1cell = WIDTH*0.15
    Height_1cell = HEIGHT*0.08
    Range_2cell = HEIGHT*0.02
    Left = WIDTH*0.1
    Right = WIDTH*0.9
    Top = HEIGHT*0.75
    
    Back = pygame.image.load('Image/assets/SetMenu/back.png')
    Help = pygame.image.load('Image/assets/SetMenu/help.png')
    Next = pygame.image.load('Image/assets/SetMenu/next.png')

    MENU_IMG = [
    pygame.transform.scale(Back, (Width_1cell, Height_1cell)),
    pygame.transform.scale(Next, (1.2*Width_1cell, 1.8*Height_1cell)),
    pygame.transform.scale(Help, (Width_1cell, Height_1cell))]
    
    # MENU LOCATION
    MENU_LOCATION = [
    (Left,Top),
    (Right-Width_1cell*1.1,Top),
    (Left,Top+(Height_1cell + Range_2cell))]
    
    # MENU OBJECT BUTTON
    MENU_OBJECT = [
    pygame.Rect(Left,Top  ,Width_1cell,Height_1cell),
    pygame.Rect(Right-Width_1cell,Top,  Width_1cell,Height_1cell),
    pygame.Rect(Left, Top+(Height_1cell + Range_2cell),Width_1cell,Height_1cell)]
    
    for i in range(0, len(MENU_OBJECT)):
        if MENU_OBJECT[i].collidepoint(mouse):
            screen.blit(MENU_IMG[i], MENU_LOCATION[i])
        else:
            screen.blit(MENU_IMG[i], MENU_LOCATION[i])

def choose_char(screen, selection_set, selection_char):
    WIDTH, HEIGHT = screen.get_size()

    # CHAR-BOARD LOCATION
    Width_1cell = WIDTH*0.12
    Height_1cell = HEIGHT*0.1
    Range_2cell = (HEIGHT*0.6-5*Height_1cell)/5
    Left = WIDTH*0.78
    Top = HEIGHT*0.08
    
    char_select = pygame.image.load('Image/Characters/ava/0.png')
    char_select = pygame.transform.scale(char_select, (Width_1cell, Height_1cell))
    light = pygame.image.load('Image/Characters/ava/ava0.png')
    light = pygame.transform.scale(light, (Width_1cell*1.2, Height_1cell*1.2))
    
    char_00 = pygame.image.load('Image/Gameplay/set0/car0.png')
    char_01 = pygame.image.load('Image/Gameplay/set0/car1.png')
    char_02 = pygame.image.load('Image/Gameplay/set0/car2.png')
    char_03 = pygame.image.load('Image/Gameplay/set0/car3.png')
    char_04 = pygame.image.load('Image/Gameplay/set0/car4.png')
    
    char_10 = pygame.image.load('Image/Gameplay/set1/car0.png')
    char_11 = pygame.image.load('Image/Gameplay/set1/car1.png')
    char_12 = pygame.image.load('Image/Gameplay/set1/car2.png')
    char_13 = pygame.image.load('Image/Gameplay/set1/car3.png')
    char_14 = pygame.image.load('Image/Gameplay/set1/car4.png')
    
    char_20 = pygame.image.load('Image/Gameplay/set2/car0.png')
    char_21 = pygame.image.load('Image/Gameplay/set2/car1.png')
    char_22 = pygame.image.load('Image/Gameplay/set2/car2.png')
    char_23 = pygame.image.load('Image/Gameplay/set2/car3.png')
    char_24 = pygame.image.load('Image/Gameplay/set2/car4.png') 
   
    
    char_30 = pygame.image.load('Image/Gameplay/set3/car0.png')
    char_31 = pygame.image.load('Image/Gameplay/set3/car1.png')
    char_32 = pygame.image.load('Image/Gameplay/set3/car2.png')
    char_33 = pygame.image.load('Image/Gameplay/set3/car3.png')
    char_34 = pygame.image.load('Image/Gameplay/set3/car4.png')

    char_40 = pygame.image.load('Image/Gameplay/set4/car0.png')
    char_41 = pygame.image.load('Image/Gameplay/set4/car1.png')
    char_42 = pygame.image.load('Image/Gameplay/set4/car2.png')
    char_43 = pygame.image.load('Image/Gameplay/set4/car3.png')
    char_44 = pygame.image.load('Image/Gameplay/set4/car4.png')
    
    set1_img = [ 
    pygame.transform.scale(char_00, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_01, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_02, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_03, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_04, (Width_1cell, Height_1cell))]
    
    set2_img = [
    pygame.transform.scale(char_10, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_11, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_12, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_13, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_14, (Width_1cell, Height_1cell))]

    set3_img = [ 
    pygame.transform.scale(char_20, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_21, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_22, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_23, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_24, (Width_1cell, Height_1cell))]
    
    set4_img = [ 
    pygame.transform.scale(char_30, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_31, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_32, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_33, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_34, (Width_1cell, Height_1cell))]
    
    set5_img = [ 
    pygame.transform.scale(char_40, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_41, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_42, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_43, (Width_1cell, Height_1cell)),
    pygame.transform.scale(char_44, (Width_1cell, Height_1cell))]
    
    list_char = set1_img
    
    # CHAR LOCATION
    CHA_LOCATION = [
    (Left,Top),
    (Left,Top+1*(Height_1cell + Range_2cell)),
    (Left,Top+2*(Height_1cell + Range_2cell)),
    (Left,Top+3*(Height_1cell + Range_2cell)),
    (Left,Top+4*(Height_1cell + Range_2cell))]
    
    # CHAR OBJECT BUTTON
    CHA_OBJECT = [
    pygame.Rect(Left,Top                               ,Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+1*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+2*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+3*(Height_1cell + Range_2cell),Width_1cell,Height_1cell),
    pygame.Rect(Left,Top+4*(Height_1cell + Range_2cell),Width_1cell,Height_1cell)]
    
    if selection_set != -1:
        if selection_set == 0: list_char = set1_img
        if selection_set == 1: list_char = set2_img
        if selection_set == 2: list_char = set3_img
        if selection_set == 3: list_char = set4_img
        if selection_set == 4: list_char = set5_img
        for i in range(0, len(CHA_OBJECT)):
            if i == selection_char:
                screen.blit(light, CHA_LOCATION[i])
                screen.blit(char_select, CHA_LOCATION[i])
                screen.blit(list_char[i], CHA_LOCATION[i]) 
            else:
                screen.blit(char_select, CHA_LOCATION[i])
                screen.blit(list_char[i], CHA_LOCATION[i]) 

def main_menu(screen, selection,LeaF,Background,moving_sprite,player):
    WIDTH, HEIGHT = screen.get_size()
    tile = WIDTH/1920
    
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

            speed = round(random.uniform(4,4.5),2)
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

    Background.draw(screen)
    player.attack()
    moving_sprite.draw(screen)
    moving_sprite.update(0.5)

    for i in range (0,21):
        LeaF[i].move(screen)

    # LAY TOA DO CON TRO CHUOT
    mouse = pygame.mouse.get_pos()
    Left = WIDTH*0.6
    Top = HEIGHT*0.2
    Bot = HEIGHT*0.9
    Width_1cell = WIDTH*0.28
    Height_1cell = (Bot-Top)/6

    Logo_game = pygame.image.load('banner/logo_banner.png')
    Logo_game = pygame.transform.scale(Logo_game, (WIDTH*0.45,HEIGHT*0.45))
    screen.blit(Logo_game, (WIDTH*0.1,HEIGHT*0.14))
    
    menu1 = pygame.image.load('img/background-menus/buttons/1.png')
    menu2 = pygame.image.load('img/background-menus/buttons/2.png') 
    menu3 = pygame.image.load('img/background-menus/buttons/3.png')
    menu4 = pygame.image.load('img/background-menus/buttons/4.png')
    menu5 = pygame.image.load('img/background-menus/buttons/6.png')
    
    menu01 = pygame.image.load('img/background-menus/buttons/01.png')
    menu02 = pygame.image.load('img/background-menus/buttons/02.png') 
    menu03 = pygame.image.load('img/background-menus/buttons/03.png')
    menu04 = pygame.image.load('img/background-menus/buttons/04.png')
    menu05 = pygame.image.load('img/background-menus/buttons/06.png')
    
    MENU_IMG = [
    pygame.transform.scale(menu1, (Width_1cell, Height_1cell)),
    pygame.transform.scale(menu2, (Width_1cell, Height_1cell)),
    pygame.transform.scale(menu3, (Width_1cell, Height_1cell)),
    pygame.transform.scale(menu4, (Width_1cell, Height_1cell)),
    pygame.transform.scale(menu5, (Width_1cell, Height_1cell)),]
    
    MENU_Click = [
    pygame.transform.scale(menu01, (Width_1cell, Height_1cell)),
    pygame.transform.scale(menu02, (Width_1cell, Height_1cell)),
    pygame.transform.scale(menu03, (Width_1cell, Height_1cell)),
    pygame.transform.scale(menu04, (Width_1cell, Height_1cell)),
    pygame.transform.scale(menu05, (Width_1cell, Height_1cell)),]
    
    # MENU OBJECT
    MENU_OBJECT = [
    pygame.Rect(Left, Top,                Width_1cell, Height_1cell),
    pygame.Rect(Left, Top+1*Height_1cell, Width_1cell, Height_1cell),
    pygame.Rect(Left, Top+2*Height_1cell, Width_1cell, Height_1cell),
    pygame.Rect(Left, Top+3*Height_1cell, Width_1cell, Height_1cell),
    pygame.Rect(Left, Top+4*Height_1cell, Width_1cell, Height_1cell)]
    
    # MENU LOCATION
    MENU_LOC = [
    (Left,Top               ),
    (Left,Top+1*Height_1cell),
    (Left,Top+2*Height_1cell),
    (Left,Top+3*Height_1cell),
    (Left,Top+4*Height_1cell)]
    
    # MENU===============================================================================
    for i in range(0, len(MENU_OBJECT)):
        if MENU_OBJECT[i].collidepoint(mouse) or selection == i+1:
            screen.blit(MENU_Click[i], MENU_LOC[i])
        else:
            screen.blit(MENU_IMG[i], MENU_LOC[i])
        Top+=Height_1cell
    # MENU===============================================================================
    Background.update()

    for i in range (0,21):
        if LeaF[i].y > HEIGHT or LeaF[i].x < 0:
            temp_leaf = leaf()
            LeaF[i] = temp_leaf

def help(screen, usernane, selection_help):
    WIDTH, HEIGHT = screen.get_size()
    Width_1cell = WIDTH*0.18
    Height_1cell = HEIGHT*0.1
    help_width = WIDTH*0.6
    help_height = HEIGHT*0.8
    Left = (WIDTH*0.5) - Width_1cell/2
    Top = HEIGHT*0.8
    
    bg_help = pygame.image.load('Image/assets/Options/bg1.png')
    bg_help = pygame.transform.scale(bg_help, (WIDTH, HEIGHT))
    
    Back = pygame.image.load('Image/assets/SetMenu/Back.png')
    Back = pygame.transform.scale(Back, (Width_1cell,Height_1cell))
    Back1 = pygame.image.load('Image/assets/Mode/back-hover.png')
    Back1 = pygame.transform.scale(Back1, (Width_1cell,Height_1cell))
    
    Arrow_next = pygame.image.load('Image/assets/Help/left.png')
    Arrow_next = pygame.transform.scale(Arrow_next, (Height_1cell,Height_1cell))
    Arrow_back = pygame.image.load('Image/assets/Help/right.png')
    Arrow_back = pygame.transform.scale(Arrow_back, (Height_1cell,Height_1cell))
    
    help = pygame.image.load('Image/assets/Help/Help2/' + str(selection_help) +'.png')
    help = pygame.transform.scale(help, (WIDTH, HEIGHT))
    
    screen.blit(help, (0,0))
    
    #  OBJECT
    HELP_OBJECT = [
    pygame.Rect(WIDTH*0.12, HEIGHT*0.45, Height_1cell, Height_1cell),
    pygame.Rect(WIDTH*0.88 - Height_1cell, HEIGHT*0.45, Height_1cell, Height_1cell),
    pygame.Rect(Left, Top, Width_1cell, Height_1cell)]
    
    #  LOCATION
    HELP_LOC = [
    (WIDTH*0.12, HEIGHT*0.45),
    (WIDTH*0.88 - Height_1cell, HEIGHT*0.45),
    (Left, Top)]
    # MOUSE LOCATION
    mouse = pygame.mouse.get_pos()
    for i in range(0, len(HELP_OBJECT)):
        if HELP_OBJECT[i].collidepoint(mouse):
            screen.blit(Arrow_back, HELP_LOC[0])
            screen.blit(Arrow_next, HELP_LOC[1])
            screen.blit(Back1, HELP_LOC[2])

def minigame1(screen, usernane):
    WIDTH, HEIGHT = screen.get_size()
    Width_1cell = WIDTH*0.14
    Height_1cell = HEIGHT*0.08
    Left = (WIDTH*0.48) - Width_1cell
    Top = HEIGHT*0.87
    #huong dan choi minigame
    bg_mini = pygame.image.load('Image/assets/Help/Help2/9.png')
    bg_mini = pygame.transform.scale(bg_mini, (WIDTH, HEIGHT))
    
    Back = pygame.image.load('Image/assets/Mode/back-hover.png')
    Back = pygame.transform.scale(Back, (Width_1cell,Height_1cell))
    minigame = pygame.image.load('Image/assets/Mode/start-hover.png')
    minigame = pygame.transform.scale(minigame, (Width_1cell,Height_1cell))
    
    # MINIGAME OBJECT
    MNG_OBJECT = [
    pygame.Rect(Left,                            Top, Width_1cell, Height_1cell),
    pygame.Rect(Left + Width_1cell + 0.04*WIDTH, Top, Width_1cell, Height_1cell)]
    
    # MINIGAME LOCATION
    MNG_LOC = [
    (Left                           , Top),
    (Left + Width_1cell + WIDTH*0.04, Top)]
    
    screen.blit(bg_mini, (0, 0))
    screen.blit(Back, MNG_LOC[0])
    screen.blit(minigame, MNG_LOC[1])

def minigame2(screen, usernane):
    WIDTH, HEIGHT = screen.get_size()
    Width_1cell = WIDTH*0.14
    Height_1cell = HEIGHT*0.08
    Left = (WIDTH*0.48) - Width_1cell
    Top = HEIGHT*0.87
    #huong dan choi minigame
    bg_mini = pygame.image.load('Image/assets/Help/Help2/10.png')
    bg_mini = pygame.transform.scale(bg_mini, (WIDTH, HEIGHT))
    
    Back = pygame.image.load('Image/assets/Mode/back-hover.png')
    Back = pygame.transform.scale(Back, (Width_1cell,Height_1cell))
    minigame = pygame.image.load('Image/assets/Mode/start-hover.png')
    minigame = pygame.transform.scale(minigame, (Width_1cell,Height_1cell))
    
    # MINIGAME OBJECT
    MNG_OBJECT = [
    pygame.Rect(Left,                            Top, Width_1cell, Height_1cell),
    pygame.Rect(Left + Width_1cell + 0.04*WIDTH, Top, Width_1cell, Height_1cell)]
    
    # MINIGAME LOCATION
    MNG_LOC = [
    (Left                           , Top),
    (Left + Width_1cell + WIDTH*0.04, Top)]
    
    screen.blit(bg_mini, (0, 0))
    screen.blit(Back, MNG_LOC[0])
    screen.blit(minigame, MNG_LOC[1])

def options(screen, username):
    WIDTH, HEIGHT = screen.get_size()
    Width_1Cell = WIDTH*0.2
    Height_1Cell = WIDTH*0.04
    Range = WIDTH*0.015
    Left = WIDTH*0.18
    Top  = HEIGHT*0.35
    
    bg = pygame.image.load('Image/assets/Options/bg2.png')
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
    
    button_light = pygame.image.load('Image/assets/Options/silver.png')
    button_light = pygame.transform.scale(button_light, (Width_1Cell, Height_1Cell))
    button_dark  = pygame.image.load('Image/assets/Options/blue.png')
    button_dark  = pygame.transform.scale(button_dark, (Width_1Cell, Height_1Cell))
    
    but1 = pygame.image.load('Image/assets/Options/1.png')
    but2 = pygame.image.load('Image/assets/Options/2.png')
    but3 = pygame.image.load('Image/assets/Options/3.png')
    but4 = pygame.image.load('Image/assets/Options/4.png')
    but5 = pygame.image.load('Image/assets/Options/5.png')
    
    BUT_IMG = [
    pygame.transform.scale(but1, (Width_1Cell, Height_1Cell)),
    pygame.transform.scale(but2, (Width_1Cell, Height_1Cell)),
    pygame.transform.scale(but3, (Width_1Cell, Height_1Cell)),
    pygame.transform.scale(but4, (Width_1Cell, Height_1Cell)),
    pygame.transform.scale(but5, (Width_1Cell, Height_1Cell))]
    
    BUT_LOC = [
    (Left, Top),
    (Left, Top+1*(Height_1Cell+Range)),
    (Left, Top+2*(Height_1Cell+Range)),
    (Left, Top+3*(Height_1Cell+Range)),
    (Left, Top+4*(Height_1Cell+Range))]
    
    BUT_OBJ = [
    pygame.Rect(Left, Top, Width_1Cell, Height_1Cell),
    pygame.Rect(Left, Top+1*(Height_1Cell+Range), Width_1Cell, Height_1Cell),
    pygame.Rect(Left, Top+2*(Height_1Cell+Range), Width_1Cell, Height_1Cell),
    pygame.Rect(Left, Top+3*(Height_1Cell+Range), Width_1Cell, Height_1Cell),
    pygame.Rect(Left, Top+4*(Height_1Cell+Range), Width_1Cell, Height_1Cell)]
    
    screen.blit(bg, (0, 0))
    mouse = pygame.mouse.get_pos()
    for i in range(0, len(BUT_OBJ)):
        if BUT_OBJ[i].collidepoint(mouse):
            screen.blit(button_dark, BUT_LOC[i])
            screen.blit(BUT_IMG[i], BUT_LOC[i])
        else:
            screen.blit(button_light, BUT_LOC[i])
            screen.blit(BUT_IMG[i], BUT_LOC[i])
    
    ON  = pygame.image.load('Image/assets/Options/on.png')
    ON  = pygame.transform.scale(ON, (Width_1Cell, Height_1Cell))
    OFF = pygame.image.load('Image/assets/Options/off.png')
    OFF = pygame.transform.scale(OFF, (Width_1Cell, Height_1Cell))
    SOUND_ON = pygame.Rect(WIDTH*0.7, Top, Width_1Cell, Height_1Cell)
    SOUND_OFF = pygame.Rect(WIDTH*0.7, Top+1*(Height_1Cell+Range), Width_1Cell, Height_1Cell)
    
    if SOUND_ON.collidepoint(mouse):
        screen.blit(button_dark, (WIDTH*0.7, Top))
        screen.blit(ON, (WIDTH*0.7, Top))
    else:
        screen.blit(button_light, (WIDTH*0.7, Top))
        screen.blit(ON, (WIDTH*0.7, Top))
        
    if SOUND_OFF.collidepoint(mouse):
        screen.blit(button_dark, (WIDTH*0.7, Top+1*(Height_1Cell+Range)))
        screen.blit(OFF, (WIDTH*0.7, Top+1*(Height_1Cell+Range)))
    else:
        screen.blit(button_light, (WIDTH*0.7, Top+1*(Height_1Cell+Range)))
        screen.blit(OFF, (WIDTH*0.7, Top+1*(Height_1Cell+Range)))

def credits(screen):
    # Set the background
    background = pygame.image.load('assets/background-menus-main.png')
    background = pygame.transform.scale(background, screen.get_size())
    screen.blit(background, (0,0));


def choose_bet(screen, set_char, char_name, rename, tiencuoc, mode):
    WIDTH, HEIGHT = screen.get_size()
    background = pygame.image.load('Image/bet/choose_bet.png').convert()
    background = pygame.transform.scale(background, (WIDTH,HEIGHT))
    screen.blit(background, (0,0))
    
    check = click.chuyenthongtin()
    tongtien = ioexcel.layTongtien(check[3])

    char_select = pygame.image.load('Image/Characters/ava/0.png')
    char_select = pygame.transform.scale(char_select, (WIDTH*0.12, HEIGHT*0.1))
    #text box
    maintext_box  = pygame.image.load('Image/assets/set_0.png')
    maintext_box  = pygame.transform.scale(maintext_box, (WIDTH*0.3, HEIGHT*0.05))

    set = 'set' + str(int(set_char//10))
    char0 = pygame.image.load('Image/Gameplay/'+ set + '/car0.png')
    char1 = pygame.image.load('Image/Gameplay/'+ set + '/car1.png')
    char2 = pygame.image.load('Image/Gameplay/'+ set + '/car2.png')
    char3 = pygame.image.load('Image/Gameplay/'+ set + '/car3.png')
    char4 = pygame.image.load('Image/Gameplay/'+ set + '/car4.png')
    
    if set_char%10 == 1:
        char1, char0 = char0, char1
    if set_char%10 == 2:
        char2, char0 = char0, char2
    if set_char%10 == 3:
        char3, char0 = char0, char3
    if set_char%10 == 4:
        char4, char0 = char0, char4

    CHAR_IMG =pygame.transform.scale(char0, (WIDTH*0.28, HEIGHT*0.5))  #3/1/2023
    
    # LAY TOA DO CON TRO CHUOT
    CENTER = WIDTH/2
    Left = CENTER*0.7 
    Right = CENTER*1.3
    Top = HEIGHT*0.6
    Bot = HEIGHT*0.9
    Width_1cell = CENTER*0.6
    Height_1cell = (Bot-Top)/5
    
    # CHAR LOCATION
    CHA_LOCATION = (WIDTH*0.13,  HEIGHT*0.15)
    
    # CHAR OBJECT BUTTON
    CHA_OBJECT = pygame.Rect(WIDTH*0.13,  HEIGHT*0.15,WIDTH*0.3,  HEIGHT*0.55) #3/1/2023    
    base_font = pygame.font.Font('Font/Gamefont.ttf', 20)
    
    screen.blit(CHAR_IMG, CHA_LOCATION)
    
    #for i in range(1, len(CHA_OBJECT)):
    screen.blit(char_select, CHA_LOCATION)
    screen.blit(CHAR_IMG, CHA_LOCATION)
    #input ten ingame
    text_surface = base_font.render(char_name, True, (255, 255, 255))
    if char_name == '':
        notext = base_font.render('Ingame Name', True, (255, 255, 255))
        screen.blit(notext, CHA_LOCATION)
    else:
        screen.blit(text_surface, CHA_LOCATION)
    screen.blit(maintext_box, CHA_LOCATION)
    text_surface = base_font.render(char_name, True, (255, 255, 255))
    screen.blit(text_surface, CHA_LOCATION)

    namefont = pygame.font.Font('Font/Gamefont.ttf',int(WIDTH*0.03))
    textbet = namefont.render('Select the bet',True,(255,255,255))
    screen.blit(textbet,(WIDTH*0.63,HEIGHT*0.08))
    betlight     = pygame.image.load('Image/assets/Mode/cost1.png')
    betlight     = pygame.transform.scale(betlight, (WIDTH*0.15, HEIGHT*0.1))
    betdark      = pygame.image.load('Image/assets/Mode/cost2.png')
    betdark      = pygame.transform.scale(betdark, (WIDTH*0.15, HEIGHT*0.1))


    bet1 = pygame.image.load('Image/assets/Mode/100.png')
    bet2 = pygame.image.load('Image/assets/Mode/500.png')
    bet3 = pygame.image.load('Image/assets/Mode/half.png')
    bet4 = pygame.image.load('Image/assets/Mode/200.png')
    bet5 = pygame.image.load('Image/assets/Mode/1000.png')
    bet6 = pygame.image.load('Image/assets/Mode/allin.png')
    checkbet = [100,500, tongtien/2 , 200, 1000, tongtien]
    BET_IMG = [
    pygame.transform.scale(bet1, (WIDTH*0.15, HEIGHT*0.1)),
    pygame.transform.scale(bet2, (WIDTH*0.15, HEIGHT*0.1)),
    pygame.transform.scale(bet3, (WIDTH*0.15, HEIGHT*0.1)),
    pygame.transform.scale(bet4, (WIDTH*0.15, HEIGHT*0.1)),
    pygame.transform.scale(bet5, (WIDTH*0.15, HEIGHT*0.1)),
    pygame.transform.scale(bet6, (WIDTH*0.15, HEIGHT*0.1))]
    
    start     = pygame.image.load('Image/assets/Mode/play1.png') # start luc dau
    start     = pygame.transform.scale(start, (WIDTH*0.18, HEIGHT*0.15))
    start1    = pygame.image.load('Image/assets/Mode/play2.png') # start luc sau
    start1    = pygame.transform.scale(start1, (WIDTH*0.18, HEIGHT*0.15))
    
    START_OBJECT = pygame.Rect(5*WIDTH*0.13 + 100,HEIGHT*0.71,WIDTH*0.18, HEIGHT*0.15)
    mouse = pygame.mouse.get_pos()
    if START_OBJECT.collidepoint(mouse):
        screen.blit(start1, (START_OBJECT[0], START_OBJECT[1]))
    else:
        screen.blit(start, (START_OBJECT[0], START_OBJECT[1]))
    
    BET_LOCATION = [
    (WIDTH*0.55,HEIGHT*0.15),
    (WIDTH*0.55,HEIGHT*0.15 + 1*HEIGHT*0.1 + HEIGHT*0.03),
    (WIDTH*0.55,HEIGHT*0.15 + 2*HEIGHT*0.1 + HEIGHT*0.03*2),
    (WIDTH*0.74, HEIGHT*0.15),
    (WIDTH*0.74, HEIGHT*0.15 + 1*HEIGHT*0.1 + HEIGHT*0.03),
    (WIDTH*0.74, HEIGHT*0.15 + 2*HEIGHT*0.1 + HEIGHT*0.03*2)]
    
    BET_OBJECT = [
    pygame.Rect(WIDTH*0.55,  HEIGHT*0.15                ,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.55,  HEIGHT*0.15 + 1*HEIGHT*0.1 + HEIGHT*0.03  ,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.55,  HEIGHT*0.15 + 2*HEIGHT*0.1 + HEIGHT*0.03*2,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.74, HEIGHT*0.15                  ,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.74, HEIGHT*0.15 + 1*HEIGHT*0.1 + HEIGHT*0.03,WIDTH*0.15, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.74, HEIGHT*0.15 + 2*HEIGHT*0.1 + HEIGHT*0.03*2,WIDTH*0.15, HEIGHT*0.1)]

    global tien
    
    if check[0] <= tien:
        for i in range(0, len(BET_OBJECT)):
            if checkbet[i]==check[0]:
                screen.blit(betlight, BET_LOCATION[i])
            else:
                screen.blit(betdark, BET_LOCATION[i])
            screen.blit(BET_IMG[i], BET_LOCATION[i])
    else:
        screen.blit(betlight, BET_LOCATION[0])
        screen.blit(BET_IMG[0], BET_LOCATION[0])
        for i in range(1, len(BET_OBJECT)):
            screen.blit(betdark, BET_LOCATION[i])
            screen.blit(BET_IMG[i], BET_LOCATION[i])
        
    MODE_LOCATION = [
    (WIDTH*0.55, HEIGHT*0.3 + 3*HEIGHT*0.1),
    (WIDTH*0.67, HEIGHT*0.3 + 3*HEIGHT*0.1),
    (WIDTH*0.79, HEIGHT*0.3 + 3*HEIGHT*0.1)]
    
    # MODe OBJECT BUTTON
    MODE_OBJECT = [
    pygame.Rect(WIDTH*0.55, HEIGHT*0.3 + 3*HEIGHT*0.1,WIDTH*0.1, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.67, HEIGHT*0.3 + 3*HEIGHT*0.1,WIDTH*0.1, HEIGHT*0.1),
    pygame.Rect(WIDTH*0.79, HEIGHT*0.3 + 3*HEIGHT*0.1,WIDTH*0.1, HEIGHT*0.1)]
    
    mode0     = pygame.image.load('Image/assets/Mode/mode.png')
    mode0     = pygame.transform.scale(mode0, (WIDTH*0.1, HEIGHT*0.08))
    
    mode1 = pygame.image.load('Image/assets/Mode/easy1.png')
    mode2 = pygame.image.load('Image/assets/Mode/normal1.png')
    mode3 = pygame.image.load('Image/assets/Mode/hard1.png')
    
    mode4 = pygame.image.load('Image/assets/Mode/easy2.png')
    mode5 = pygame.image.load('Image/assets/Mode/normal2.png')
    mode6 = pygame.image.load('Image/assets/Mode/hard2.png')
    
    MODE_IMG = [
    pygame.transform.scale(mode1, (WIDTH*0.1, HEIGHT*0.08)),
    pygame.transform.scale(mode2, (WIDTH*0.1, HEIGHT*0.08)),
    pygame.transform.scale(mode3, (WIDTH*0.1, HEIGHT*0.08)),
    pygame.transform.scale(mode4, (WIDTH*0.1, HEIGHT*0.08)),
    pygame.transform.scale(mode5, (WIDTH*0.1, HEIGHT*0.08)),
    pygame.transform.scale(mode6, (WIDTH*0.1, HEIGHT*0.08))]
    checkmode = [2,3,4]
    mouse = pygame.mouse.get_pos()
    
    for i in range(0, 3):
        if MODE_OBJECT[i].collidepoint(mouse) or mode == 2*i+1:
            screen.blit(mode0, MODE_LOCATION[i])
            screen.blit(MODE_IMG[i+3], MODE_LOCATION[i])
        else:
            screen.blit(mode0, MODE_LOCATION[i])
            if checkmode[i] == check[1]:
                screen.blit(MODE_IMG[i+3], MODE_LOCATION[i])
            else:
                screen.blit(MODE_IMG[i], MODE_LOCATION[i])
            
    Back = pygame.image.load('Image/assets/SetMenu/back.png')
    Back = pygame.transform.scale(Back, ( WIDTH*0.12, HEIGHT*0.07))
    Back1 = pygame.image.load('Image/assets/Mode/back-hover.png')
    Back1 = pygame.transform.scale(Back1, ( WIDTH*0.12, HEIGHT*0.07))
    
    BACK_LOCATION = (WIDTH*0.08, HEIGHT*0.85)
    BACK_BUTTON = pygame.Rect(WIDTH*0.08,HEIGHT*0.85, WIDTH*0.12, HEIGHT*0.07)
    mouse = pygame.mouse.get_pos()
    if BACK_BUTTON.collidepoint(mouse):
        screen.blit(Back1, BACK_LOCATION)
    else:
        screen.blit(Back, BACK_LOCATION)