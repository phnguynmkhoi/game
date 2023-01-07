from math import sqrt
import random
import pygame

#intialize pygame
pygame.init()



def minigame1():
    #Adjust to resize screen
    global maxW,maxH,score,enemyEdge,laserState,playerX,eX,diLaserX,playerY,eY,diLaserY,dis,disX,disY,laserX,laserY,coinState,coinX,coinY,restart,difficulty
    global alive,playerX,playerY,scoreText
    maxW,maxH=900,500   
    screen= pygame.display.set_mode((maxW,maxH))

    #Background
    background= pygame.image.load("minigame1/img/starbg.jpg")
    pygame.mixer.music.load('minigame1/soundEffect/background.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.05)

    #Title and background and Font
    pygame.display.set_caption("Hello World")
    icon= pygame.image.load('minigame1/img/logo.png')
    pygame.display.set_icon(icon)
    gameover= pygame.image.load('minigame1/img/gameover.png')
    font = pygame.font.Font('freesansbold.ttf',32)
    fontI= pygame.font.Font('minigame1/font/static/Nunito-Italic.ttf',24)

    #Animation
    explode = pygame.image.load('minigame1/img/explode.png')
    explodeSound = pygame.mixer.Sound('minigame1/soundEffect/explosion.wav')
    explodeSound.set_volume(0.05)

    #Score
    textX,textY=5,5
    score=0
    scoreText=font.render(("Coin:"+ str(score)),True,(255,255,255))

    #Coin
    coinImg=[]
    for i in range(8):
        img=f"minigame1/img/coin_{i}.png"
        coinImg.append(pygame.image.load(img))# Trying to add a gif instead of png file
    coinEdge=24
    coinX,coinY=random.randint(6,maxW-coinEdge),random.randint(6,maxH-coinEdge)
    coinState=1
    difficulty=0
    curSprite=0

    #Laser
    laserImg=pygame.image.load("minigame1/img/medical.png")
    laserState=[]
    laserX,laserY=[],[]
    disX,disY,dis=[],[],[]
    diLaserX,diLaserY=[],[]
    laserEdge=24
    laserSound= pygame.mixer.Sound('minigame1/soundEffect/laser.wav')
    laserSound.set_volume(0.05)

    #Player
    playerImg=pygame.image.load("minigame1/img/worldwide.png")
    playerX,playerY= 268,250
    changeX,changeY=0,0
    playerEdge=24
    alive=1

    #enemies
    enemiesImg=pygame.image.load("minigame1/img/ufo.png")
    eX,eY,diX,diY=[],[],[],[]
    enemyEdge=64

    #Time
    curTime=0

    #Restart
    restart=0
    restartText= fontI.render('Click anywhere to restart',True, (120,255,255))

    print(fontI.size("Click anywhere to continue"))
    #Continue

    def draw(State,x,y):
        screen.blit(State,(x,y))

    def fire(i):
        laserSound.play()
        global playerX,playerY,eX,eY,laserX,laserY,laserState,diLaserX,diLaserY,dis,disX,disY
        laserState[i]=1
        diLaserX[i]= abs(playerX-eX[i])/(playerX-eX[i])
        diLaserY[i]= abs(playerY-eY[i])/(playerY-eY[i])
        dis[i]=sqrt((playerY-eY[i])*(playerY-eY[i])+(playerX-eX[i])*(playerX-eX[i]))
        disX[i],disY[i]=abs(playerX-eX[i]),abs(playerY-eY[i])
        laserX[i],laserY[i]= eX[i],eY[i]

    def newCoin():
        global coinX,coinY,score,coinState
        coinState=1
        # score+=1
        coinX=random.randint(6,maxW-coinEdge)
        coinY=random.randint(6,maxH-coinEdge)

    def isCollide(a,b,x,y):
        if sqrt((a-x)*(a-x)+(b-y)*(b-y))< 30:
            return 1
        return 0
        
    def bounce(i):
        if eX[i]<=0:
            diX[i]=random.uniform(1,1.3)
        if eX[i]>=maxW-enemyEdge:
            diX[i]=-random.uniform(1,1.3)
        if eY[i]<=0:
            diY[i]=random.uniform(1,1.3)
        if eY[i]>=maxH-enemyEdge:
            diY[i]=-random.uniform(1,1.3)

    def increaseDifficulty():
        global enemyEdge
        eX.append(random.choice([-enemyEdge,maxW+10]))
        eY.append(random.choice([-enemyEdge,maxH+10]))
        diX.append(0)
        diY.append(0)
        laserX.append(0.1)
        laserY.append(0.1)
        laserState.append(0)
        dis.append(0)
        disX.append(0)
        disY.append(0)
        diLaserX.append(0)
        diLaserY.append(0)
        bounce(len(eX)-1)

    def setRestart():
        global score,alive,playerX,playerY,difficulty,scoreText
        eX.clear()
        eY.clear()
        diX.clear()
        diY.clear()
        laserX.clear()
        laserY.clear()
        laserState.clear()
        dis.clear()
        disX.clear()
        disY.clear()
        diLaserX.clear()
        diLaserY.clear()
        score=0
        alive=1
        playerX,playerY= 268,250
        difficulty=0
        scoreText=font.render(("Coin:"+ str(score)),True,(255,255,255))
        
    #Game Loop
    running= True

    while running:
        screen.fill((4,4,4))
        screen.blit(background,(0,0))
        # tmp=pygame.display.get_window_size()
        # print (tmp)
        #Event
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                running=False
            # if event.type== pygame.VIDEORESIZE:
            #     screen=pygame.display.set_mode((event.h,event.w),pygame.VIDEORESIZE)
            if event.type== pygame.MOUSEBUTTONDOWN and restart==1:
                setRestart()
                restart=0
            if alive==1 and event.type== pygame.KEYDOWN:
                if event.key== pygame.K_LEFT:
                    changeX-=0.5*(maxW/600)
                if event.key== pygame.K_RIGHT:
                    changeX+=0.5*(maxW/600)
                if event.key== pygame.K_DOWN:
                    changeY+=0.5*(maxW/600)
                if event.key== pygame.K_UP:
                    changeY-=0.5*(maxW/600)
            
            if event.type== pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key== pygame.K_RIGHT:
                    changeX=0
                if event.key==pygame.K_DOWN or event.key== pygame.K_UP:
                    changeY=0
        
        #increaseDifficulty
        if score>=difficulty*5 and len(eX)<5 and score>=1:
            difficulty+=1
            increaseDifficulty()

        #enenmyMovement
        for i in range(len(eX)):
            bounce(i)
            eX[i] += 0.1*(maxW/600)*diX[i]
            eY[i] += 0.1*(maxW/600)*diY[i]
            draw(enemiesImg,eX[i],eY[i])

        #laserMovement
        for i in range (len(laserX)):
            if laserState[i] == 0 and alive==1 :
                fire(i)
            if laserX[i]< -laserEdge or laserX[i]>maxW or laserY[i]< -laserEdge or laserY[i]>maxH:
                laserState[i]=0
            
            laserX[i]+= 0.3*(maxW/600)*disX[i]/dis[i] * diLaserX[i]
            laserY[i]+= 0.3*(maxW/600)*disY[i]/dis[i] * diLaserY[i]
            if laserState[i]!=2:
                draw(laserImg,laserX[i],laserY[i])

        #Collision
        for i in range (len(eX)):
            if (isCollide(playerX,playerY,eX[i],eY[i]) or isCollide(playerX,playerY,laserX[i],laserY[i])) and alive==1:
                alive=0
                laserState[i]=2
                timeCnt=pygame.time.get_ticks()
                explodeSound.play()
                
        if isCollide(playerX,playerY,coinX,coinY) and coinState==1 :
            score+=1
            coinState=0
            scoreText=font.render(("Coin: "+ str(score)),True,(255,255,255))
            newCoin()

        if curSprite>=8 and coinState==1:
            curSprite=0    
        curSprite+=0.014
        draw(coinImg[int(curSprite)%7],coinX,coinY)

        #playerMovement
        if alive==1:
            draw(playerImg,playerX,playerY)
        else :
            # Lose
            
            if curTime - timeCnt <=1000:
                draw(explode,playerX-48,playerY-48)
            elif curTime- timeCnt >=1500:
                draw(gameover,270,70)
            if curTime-timeCnt >=2000:
                restart=1
                draw(restartText,305,360)
            changeX,changeY=0,0
            
        if 0<playerX+changeX<maxW-laserEdge:
            playerX+=changeX
        if 0<playerY+changeY<maxH-laserEdge:
            playerY+=changeY
        #Score
        draw(scoreText,textX,textY)
        #Time
        curTime=pygame.time.get_ticks()

        pygame.display.update()
        # break
minigame1()
