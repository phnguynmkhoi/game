import pygame
import random
import math

def rand():
    a=random.randint(0,3)
    b=random.randint(0,3)
    while a==b:
        b=random.randint(0,3)
    return [a,b]

def draw(player_car,x,y):
    screen.blit(player_car,(x, y))
def isCollide(a,b,x,y):
    return (math.sqrt((a-x)*(a-x)+(b-y)*(b-y))<screen.get_width()/12.5)

def distance(a,b,x,y):
    return math.sqrt((a-x)*(a-x)+(b-y)*(b-y))

class CAR:
    def __init__(self, car_y,ratio ,velocity,curRound):
        self.spriteWheel = []
        self.x = 0
        self.y = car_y/ratio
        self.velocity = velocity
        self.destination = 0
        self.curRound=curRound
        self.ratio=ratio
        self.duration=random.uniform(2000,3000)
        self.curSpriteWheel=0
        self.curSpriteSmoke=0
        self.spriteSmoke=[]
        self.pivotTime=0
        self.smokeX=0
    def run(self):
        if curTime-self.pivotTime>= self.duration and self.velocity!=0:
            tmp=random.uniform(self.velocity-0.3,second_velocity)
            if tmp>=self.velocity:
                self.curSpriteSmoke=0
                self.velocity=tmp
            self.pivotTime=curTime
            self.smokeX=self.x-screen.get_width()/33.34
        self.x += self.velocity 
    def runAnimation(self,ok):
        if ok:
            self.curSpriteWheel+=0.4
        if self.curSpriteWheel>=len(self.spriteWheel):
            self.curSpriteWheel=0
        draw(self.spriteWheel[int(self.curSpriteWheel)] ,self.x,self.y)
        self.curSpriteSmoke+=0.2
        if self.curSpriteSmoke<len(self.spriteSmoke) :
            if int(self.curSpriteSmoke)<=5  :
                self.smokeX=self.x-screen.get_width()/30
            if  self.x>self.smokeX:
                draw(self.spriteSmoke[int(self.curSpriteSmoke)],self.smokeX,self.y+screen.get_height()/28)

    def resize(self):
        w = screen.get_width()
        h = screen.get_height()
        for i in range(4):
            self.spriteWheel[i] = pygame.transform.scale(self.spriteWheel[i],(w/12.5,h/12))
        global oldWidth,first_velocity,second_velocity
        self.x = self.x * screen.get_width() / oldWidth
        self.y=h/self.ratio

class ITEM :
    def __init__(self,y,velocity):
        global mysbox
        self.curBox=0
        self.img = mysbox
        self.y=y #fixed
        self.appRound=rand()
        self.x= [random.randint(500,800),random.randint(500,800)]
        self.visible=[1,1]
        self.velocity=velocity
        self.duration=0
        self.pivotTime=0 #Set when you pick an item
        self.spriteWin=[]
        self.spriteLose=[]
        self.spriteFlash=[]
        self.spriteFlip=[]
        self.spriteLaser=[]
        self.spriteBoost=[]
        self.spriteSlow=[]
        self.spriteStun=[]
        self.curSprite=0
        self.portalX=0
        self.openPortal=0
        self.checkFlip = 0
        self.flipX=0
        self.flipVelocity=0
        self.name=10
        self.laser=0
        self.boost=0
        self.slow=0
        self.countFlip = 0
    def slower(self,i):
        self.name = 1
        self.duration=1500
        car[i].velocity=car[i].velocity/2
        self.pivotTime=pygame.time.get_ticks()
        self.slow=1
        self.curSprite=0
    def runSlow(self, i): 
        if curTime-self.pivotTime > self.duration:
            car[i].velocity = car[i].velocity
            self.slow=0
        self.curSprite+=0.3
        if car[i].curRound== car[carSelected].curRound:
            draw(self.spriteSlow[int(self.curSprite)%1],car[i].x,self.y-50)
    def faster(self,i):
        self.name = 0
        self.duration=1000 #Duration of an item
        car[i].velocity=car[i].velocity*2
        self.pivotTime= pygame.time.get_ticks()
        self.boost=1
        self.curSprite=0
    def runFaster(self,idx):
        self.curSprite+=0.3
        if car[idx].curRound==car[carSelected].curRound:
            draw(self.spriteBoost[int(self.curSprite)%7],car[idx].x-screen.get_width()/18,self.y)
        if curTime- self.pivotTime> self.duration:
            self.boost=0
            car[idx].velocity/=2
    def setLaser(self):
        self.curSprite=0    
        self.laser=1

    def runLaser(self,idx):
        self.curSprite+=0.12
        if self.curSprite<5:
            if car[idx].curRound==car[carSelected].curRound:
                draw(self.spriteLaser[int(self.curSprite)],car[idx].x,self.y-self.spriteLaser[int(self.curSprite)].get_height()+screen.get_height()/5)
        else:
            self.laser=2
            self.curSprite=0
            self.stun(idx)
            
    def stun(self,i):
        self.duration=1000 #Duration of an item
        self.velocity=car[i].velocity
        car[i].velocity = 0
        self.pivotTime = pygame.time.get_ticks()
        self.curSprite = 0
        
    def runStun(self,i):
        if curTime-self.pivotTime>self.duration:
            car[i].velocity=self.velocity
        self.curSprite += 0.1
        if car[i].curRound== car[carSelected].curRound:
                draw(self.spriteStun[int(self.curSprite)%3],car[i].x+screen.get_width()/100,car[i].y-screen.get_width()/35)
       
    
    def flip(self):
        # self.name = 2
        self.curSprite=0
        self.flipX=screen.get_width()+screen.get_width()/6.67
        self.checkFlip = 1
        self.flipVelocity=screen.get_width()/120
        self.countFlip = 0
        self.tempFlip = 0

    def runFlip(self,idx):
        if isCollide(car[idx].x,car[idx].y,self.flipX,self.y):
            if car[idx].x<self.flipX:
                car[idx].y-=0.8
            # if car[idx].x-distance(car[idx].x,car[idx].y,self.flipX,self.y)<=self.flipX:
            elif car[idx].x>self.flipX :
                car[idx].y+=0.8
            car[i].x-=2.5*car[i].velocity
            if int(self.tempFlip) == self.tempFlip:
                for j in range (len(car[idx].spriteWheel)):
                    car[i].spriteWheel[int(j)] = pygame.transform.flip(car[i].spriteWheel[int(j)],True,False)
                self.countFlip += 1
        self.tempFlip += 0.25
        self.flipX -= self.flipVelocity 
        if self.curSprite>5:
            self.curSprite=0
        self.curSprite+=0.4 
        if car[carSelected].curRound==car[idx].curRound:
            draw(self.spriteFlip[int(self.curSprite)],self.flipX,self.y-screen.get_height()/12)
        if self.flipX<-screen.get_width()/6 :
            self.checkFlip=0
            
            
    def win(self,idx):
        self.openPortal=1
        self.portalX=0
        self.out=0
        self.curSprite=0
           
    def runWin(self,idx):
        if isCollide(car[idx].x,car[idx].y,self.portalX,self.y):
            bg[mapSelected][car[idx].curRound].car.remove(idx)
            car[idx].curRound=3
            bg[mapSelected][car[idx].curRound].car.append(idx)
            if self.out==0:
                car[idx].x=screen.get_width()/1.3
                self.curSprite=4
            self.out=1
            self.portalX=screen.get_width()/1.3
        if self.out==0:    
            if self.curSprite>3:
                self.curSprite=0
        else:
            if self.curSprite>7:
                self.curSprite=4
        self.curSprite+=0.4
        if car[idx].curRound==car[carSelected].curRound:
            draw(self.spriteWin[int(self.curSprite)],self.portalX,self.y-screen.get_height()/20)
        if distance(car[idx].x,car[idx].y,self.portalX,self.y)>screen.get_width()/7.1 and self.out :
            self.openPortal=0

    def lose(self,idx):
        self.openPortal=2
        self.portalX=0
        self.out=0
        self.curSprite=0

    def runLose(self,idx):
        if isCollide(car[idx].x,car[idx].y,self.portalX,self.y):
            if self.out==0:
                car[idx].x=10
                self.curSprite=4
            self.out=1
            self.portalX=10
        if self.out==0:    
            if self.curSprite>3:
                self.curSprite=0
        else:
            if self.curSprite>7:
                self.curSprite=4
        self.curSprite+=0.4
        if car[idx].curRound==car[carSelected].curRound:
            draw(self.spriteLose[int(self.curSprite)],self.portalX,self.y-screen.get_height()/20)
        if distance(car[idx].x,car[idx].y,self.portalX,self.y)>250:
            self.openPortal=0

    def flash(self,idx):
        car[idx].x+=170
        car[idx].y=-100
        self.curSprite=0
        self.flashX= car[idx].x+10
    def runFlash(self,idx):
        if self.curSprite+0.20<5:
            self.curSprite+=0.20
        else:
            car[idx].y=self.y-20
        if car[idx].curRound == car[carSelected].curRound:
            draw(self.spriteFlash[int(self.curSprite)],self.flashX,self.y-screen.get_height()/20)
    
    def resize(self,i):
        for j in range(4):
            img = pygame.image.load(f"img/mics/stun_{j}.png")
            img = pygame.transform.scale(img,(screen.get_width()/25,screen.get_height()/20))
            self.spriteStun[j] = img
        for j in range(8):
            img = pygame.image.load(f"img/mics/{j}-nitro.png")
            img = pygame.transform.scale(img,(screen.get_width()/15,screen.get_height()/20))
            self.spriteBoost[j] = img
        for j in range (1):
            img=pygame.image.load(f"img/mics/turtle.png")
            img = pygame.transform.scale(img, (screen.get_width()/18,screen.get_height()/15))
            self.spriteSlow[j] = img
        for j in range(8):
            img=pygame.image.load(f"img/mics/portal_{j}.png")
            img = pygame.transform.scale(img,(screen.get_width()/18,screen.get_height()/8))
            self.spriteWin[j] = img
        for j in range(5):
            img=pygame.image.load(f"img/mics/flash_{j}.png")
            img = pygame.transform.scale(img,(screen.get_width()/7,screen.get_height()/7))
            self.spriteFlash[j] = img
        for j in range(8):
            img=pygame.image.load(f"img/mics/portal_lose_{j}.png")
            img = pygame.transform.scale(img,(screen.get_width()/18,screen.get_height()/8))
            self.spriteLose[j] = img
        for j in range(6):
            img=pygame.image.load(f"img/mics/flip_{j}.png")
            img = pygame.transform.scale(img, (screen.get_width()/20,screen.get_height()/6))
            self.spriteFlip[j] = img
        for j in range(5):
            img=pygame.image.load(f"img/mics/lightning_{j}.png")
            img = pygame.transform.scale(img,(screen.get_width()/14,screen.get_height()))
            self.spriteLaser[j] = img
        self.x[0] = self.x[0] * screen.get_width()/ oldWidth
        self.x[1] = self.x[1] * screen.get_width()/ oldWidth
        

class BACKGROUND:
    def __init__(self,img, start,end) :
        self.img=pygame.transform.scale(img,(screen.get_width(),screen.get_height()))
        self.start=start
        self.end=end
        self.car=[]