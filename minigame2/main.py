from math import sqrt
import random
import pygame
import math

#intialize pygame
pygame.init()
def minigame2():
    global bgX
    maxW,maxH=900,500   
    screen= pygame.display.set_mode((maxW,maxH))
    pygame.display.set_caption("Training Lee")
    pygame.display.set_icon(pygame.image.load('minigame2/img/fist.png'))

    #SOUND
    pygame.mixer.music.load('minigame2/sound/cool.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.7)
    parrySound=[]
    for i in range (1,19):
        parrySound .append( pygame.mixer.Sound(f"minigame2/sound/{i}.ogg"))
    hitted = pygame.mixer.Sound('minigame2/sound/tribe_f.wav')
    hitted.set_volume(2)
    #FONT
    fontEnd = pygame.font.Font('minigame2/font/Audiowide-Regular.ttf',104)
    fontscore=pygame.font.Font('minigame2/font/Audiowide-Regular.ttf',20)
    # fontI= pygame.font.Font('font/static/Nunito-Italic.ttf',24)

    #LINE
    gameover=fontEnd.render("Wasted",True,(200,10,10))
    score=0

    #Function
    def draw(player_car,x,y):
        screen.blit(player_car,(x, y))

    def distance(a,b,x,y):
        return sqrt((a-x)*(a-x)+(b-y)*(b-y))

    def resize(img,x,y):
        return pygame.transform.scale(img,(x,y))

    bg=pygame.image.load("minigame2/img/bg2.png")
    bg=pygame.transform.scale(bg,(bg.get_width(),maxH))
    bgX=-300
    bgY=0
    heart=resize(pygame.image.load("minigame2/img/heart.png"),32,32)
    wood=pygame.image.load("minigame2/img/wood.png")
    wood=resize(wood,160,80)
    shadow=pygame.image.load("minigame2/img/shadow.png")
    shadow=resize(shadow,50,25)
    #1 Right
    #0 Left

    spriteEnemy=[]
    for i in range(3):
        img=f"minigame2/img/shuriken_{i}.png"
        spriteEnemy.append(resize(pygame.image.load(f"minigame2/img/shuriken_{i}.png"),32,32))
    di=[-1,1]
    def newEnemy():
        a=ENEMY(random.choice([-30,maxW]),random.choice([1,0]),random.uniform(3,4))
        return a
    class ENEMY:
        def __init__(self,x,idi,velocity):
            self.curSprite=0
            self.x=x
            self.y=fighter.y+random.uniform(10,50)
            self.idi=idi
            self.velocityX=velocity
            self.velocityY=0
            self.kicked=0
        def run(self):
            self.curSprite+=1
            self.x+= self.velocityX*di[self.idi]
            if random.randint(1,7)==1:
                self.velocityX=random.uniform(3,4.5)
            self.y+= self.velocityY
            draw(spriteEnemy[int(self.curSprite)%len(spriteEnemy)],self.x,self.y)
        def kickedd(self):
            pass
            self.idi=1-self.idi
            self.velocityY=random.uniform(-3,3)
            self.velocityX=6

    class FIGHTER:
        def __init__(self):
            self.health=3
            self.width=80
            self.height=125
            self.x=400
            self.y=320
            self.rangeImg=0
            self.idleSprite=[]
            self.curIdleSprite=0
            self.AttackSprite=[]
            self.curAttSprite=0
            self.attRange=150
            self.curAttRange=0
            self.idi=0
            self.active=0
            self.targetX,self.targetY=0,0
            self.cnt=4
            self.death=[]
            self.curDeath=0
        def recover(self): #Chay khi active=0
            if self.curAttRange<self.attRange :
                self.curAttRange +=2.3   
            self.curIdleSprite+=0.1
            if self.active==0:
                draw(shadow,self.x*1.01,self.y+self.height*0.85)
                draw(self.idleSprite[self.idi][int(self.curIdleSprite)%len(self.idleSprite[di[self.idi]])],self.x,self.y)
                
            #Left
            draw(resize(self.rangeImg,self.curAttRange,10),self.x-self.curAttRange,self.y+self.height*1.05)
            #Right
            draw(resize(self.rangeImg,self.curAttRange,10),self.x+self.width*0.8,self.y+self.height*1.05)
        def setAttack(self,idi,x):
            parrySound[random.randint(0,17)].play()
            self.curAttSprite=random.choice([0,5,10,15])
            self.idi=idi
            self.active=1
            if abs(self.x-x)<=self.curAttRange*1.2:
                self.targetX=x 
            else :
                self.targetX=self.x
            self.curAttRange=20
            self.cnt=0
        def Attack(self): #Chay khi active=1
            direct=di[self.idi]
            if self.idi==0:
                if direct*self.x<direct*(self.targetX+40):
                    self.x+=15*direct
            if self.idi==1:
                if direct*self.x<direct*(self.targetX-40):
                    self.x+=15*direct
            
            self.curAttSprite+=0.2
            self.cnt+=0.2
            if self.cnt<5:
                draw(shadow,self.x*1.01,self.y+self.height*0.85)
                draw(self.AttackSprite[self.idi][int(self.curAttSprite)],self.x,self.y)
            else:
                self.active=0
        def rePosition(self):
            global bgX
            if bgX>=-3 or bgX+bg.get_width()<maxW+3 :
                return
            if self.x>455 :
                self.x-=0.6
                bgX-=0.5
            if self.x<345:
                self.x+=0.6
                bgX+=0.5
        def die(self):
            self.curDeath+=0.1
            # if self.curDeath<len(self.death):
            draw(resize(shadow,self.death[min(11,int(self.curDeath))].get_width(),shadow.get_height()),self.x*1.01,self.y+self.height*0.85)
            draw(self.death[min(11,int(self.curDeath))],self.x,self.y-self.death[min(11,int(self.curDeath))].get_height()+self.height)
            # else :
            #     draw(self.death[11],self.x,self.y+self.death[11].get_height()+self.height)
            if self.curDeath>20:
                draw(gameover,(maxW-gameover.get_width())/2,(maxH-gameover.get_height())/2)

    #INITIALIZE
    fighter=FIGHTER()

    for i in range(2):
        fighter.idleSprite.append([])
        fighter.AttackSprite.append([])
        if i==0:
            for j in range(1,13,1):
                img = pygame.image.load(f"minigame2/img/deathLee-{j}.png")
                fighter.death.append(img)
        for j in range(1,6,1):
            img = pygame.image.load(f"minigame2/img/lee-{j}.png")
            # img = resize(img,56,fighter.height)
            if i==0:
                img=pygame.transform.flip(img,True,False)
            fighter.idleSprite[i].append(img)
        #ATTACK
        for j in range(10,15,1):
            img = pygame.image.load(f"minigame2/img/lee-{j}.png")
            # img = resize(img,56,fighter.height)
            if i==0:
                img=pygame.transform.flip(img,True,False)
            fighter.AttackSprite[i].append(img)
        for j in range(18,23,1):
            img = pygame.image.load(f"minigame2/img/lee-{j}.png")
            # img = resize(img,56,fighter.height)
            if i==0:
                img=pygame.transform.flip(img,True,False)
            fighter.AttackSprite[i].append(img)
        for j in range(27,32,1):
            img = pygame.image.load(f"minigame2/img/lee-{j}.png")
            # img = resize(img,56,fighter.height)
            if i==0:
                img=pygame.transform.flip(img,True,False)
            fighter.AttackSprite[i].append(img)
        for j in range(6,11,1):
            img = pygame.image.load(f"minigame2/img/lee-{j}.png")
            img = resize(img,fighter.width,fighter.height)
            if i==0:
                img=pygame.transform.flip(img,True,False)
            fighter.AttackSprite[i].append(img)
    fighter.rangeImg=pygame.image.load("minigame2/img/rect2.png")
    enemy=[]

    ### INIT gamecd
    running =True
    clock=pygame.time.Clock()
    pivotTime=0
    end=0
    duration=random.uniform(500,900)
    fps = 120

    while running:
        clock.tick(fps)
        curTime=pygame.time.get_ticks()
        fighter.rePosition()
        draw(bg,bgX,0)
        #
        draw(wood,0,0)
        for i in range(fighter.health):
            draw(heart,(i)*36+10,10)
        scoreDisplay=fontscore.render(f"Blocked: {score}",True,(230,230,190))
        draw (scoreDisplay,10,50)
        ##   
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN and end ==0:
                if event.key==pygame.K_LEFT :
                    # fighter.setAttack(0,fighter.x)
                    maxx=0
                    ko=None
                    for e in enemy: 
                        if fighter.x-e.x<=fighter.curAttRange and fighter.x>=e.x:
                            maxx=max(e.x,maxx)
                            ko=e
                    fighter.setAttack(0,maxx)
                    if ko!=None :
                        for e in enemy:
                            if e==ko:
                                score+=1
                                e.kickedd()
                                break
                    
                if event.key==pygame.K_RIGHT :
                    minn=1300
                    ko=None
                    for e in enemy: 
                        if e.x>=fighter.x and e.x-fighter.x<=fighter.curAttRange:
                            minn=min(minn,e.x)
                            ko=e
                    if minn==1300:
                        minn=fighter.x
                        ko=None
                    fighter.setAttack(1,minn) 
                    if ko!=None :
                        for e in enemy:
                            if e==ko:
                                score+=1
                                e.kickedd()
                                break
                        

        if end==0:
            if fighter.active:
                fighter.Attack()

            fighter.recover()
        else :
            fighter.die()
        # img = pygame.image.load("img/lee-9.png")
        # img = resize(img,fighter.width,fighter.height)
        # draw(img,fighter.x,fighter.y)
        for e in enemy:
            e.run()
            if e.x<-40 or e.x>maxW+10:
                enemy.remove(e)
            if distance(e.x,fighter.y,fighter.x,fighter.y)<20 and end==0:
                enemy.remove(e)
                hitted.play()
                fighter.health-=1
                if fighter.health==0:
                    end=1
        if curTime-pivotTime>=duration and end==0:
            duration=duration=duration=random.uniform(300,500)

            pivotTime=curTime
            enemy.append(newEnemy())
        pygame.display.update()

minigame2()
    
    
        