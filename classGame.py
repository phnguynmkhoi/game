import pygame
import random

def rand():
    a=random.randint(0,3)
    b=random.randint(0,3)
    while a==b:
        b=random.randint(0,3)
    return [a,b]

class ITEM :
    def __init__(self,y,velocity):
        self.img = mysbox
        self.y=y #fixed
        self.appRound=rand()
        self.x= [random.randint(400,700),random.randint(400,700)]
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
    def slower(self,i):
        self.name = 1
        self.duration=1500
        car[i].velocity=car[i].velocity/1.5
        self.pivotTime=pygame.time.get_ticks()
        self.slow=1
        self.curSprite=0
    def runSlow(self, i): 
        if curTime-self.pivotTime > self.duration:
            car[i].velocity = car[i].velocity*1.5
            self.slow=0
        self.curSprite+=0.3
        if car[i].curRound== car[carSelected].curRound:
            draw(self.spriteSlow[int(self.curSprite)%1],car[i].x,self.y-50)
    def faster(self,i):
        self.name = 0
        self.duration=1000 #Duration of an item
        car[i].velocity=car[i].velocity*1.5
        self.pivotTime= pygame.time.get_ticks()
        self.boost=1
        self.curSprite=0
    def runFaster(self,idx):
        self.curSprite+=0.3
        if car[idx].curRound==car[carSelected].curRound:
            draw(self.spriteBoost[int(self.curSprite)%7],car[idx].x-55,self.y)
        if curTime- self.pivotTime> self.duration:
            self.boost=0
            car[idx].velocity/=1.5
    def setLaser(self):
        self.curSprite=0    
        self.laser=1

    def runLaser(self,idx):
        self.curSprite+=0.08
        if self.curSprite<5:
            if car[idx].curRound==car[carSelected].curRound:
                draw(self.spriteLaser[int(self.curSprite)],car[idx].x,self.y-self.spriteLaser[int(self.curSprite)].get_height()+130)
        else:
            self.laser=2
            self.curSprite=0
            self.stun(idx)
    def stun(self,i):
        self.duration=1000 #Duration of an item
        car[i].velocity = 0
        self.pivotTime = pygame.time.get_ticks()
        self.curSprite = 0
    def runStun(self,i):
        self.name = 3
        if (car[i].velocity == 0):
            self.curSprite += 0.1
            if car[i].curRound== car[carSelected].curRound:
                 draw(self.spriteStun[int(self.curSprite)%3],car[i].x+screen.get_width()/100,car[i].y-screen.get_width()/35)
       
    
    def flip(self):
        # self.name = 2
        self.curSprite=0
        self.flipX=screen.get_width()+150
        self.checkFlip = 1
        self.flipVelocity=7
        # car[i].velocity = -1 * car[i].velocity
        # for j in range(4):
        #     car[i].img[j] = pygame.transform.flip(car[i].img[j],True,False)

    def runFlip(self,idx):
        if isCollide(car[idx].x,car[idx].y,self.flipX,self.y):
            if car[idx].x<self.flipX:
                car[idx].y-=0.8
            # if car[idx].x-distance(car[idx].x,car[idx].y,self.flipX,self.y)<=self.flipX:
            elif car[idx].x>self.flipX :
                car[idx].y+=0.8
            car[i].x-=2.5*car[i].velocity
        self.flipX -= self.flipVelocity
        if self.curSprite>5:
            self.curSprite=0
        self.curSprite+=0.4 
        if car[carSelected].curRound==car[idx].curRound:
            draw(self.spriteFlip[int(self.curSprite)],self.flipX,self.y-55)
        if self.flipX<-100 :
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
            draw(self.spriteWin[int(self.curSprite)],self.portalX,self.y-30)
        if distance(car[idx].x,car[idx].y,self.portalX,self.y)>140 and self.out :
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
            draw(self.spriteLose[int(self.curSprite)],self.portalX,self.y-30)
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
            draw(self.spriteFlash[int(self.curSprite)],self.flashX,self.y-30)

class BACKGROUND:
    def __init__(self,img, start,end) :
        self.img=pygame.transform.scale(img,(screen.get_width(),screen.get_height()))
        self.start=start
        self.end=end
        self.car=[]

class CAR:
    def __init__(self, car_y,ratio ,velocity,curRound):
        self.img = []
        self.x = 0
        self.y = car_y/ratio
        self.velocity = velocity
        self.destination = 0
        self.curRound=curRound
        self.oldWidth = screen.get_width()
        self.ratio=ratio
        self.duration=random.uniform(1000,1600)
        self.curSprite=0
        self.pivotTime=0
    def addImg(self,img):
        self.img.append(pygame.transform.scale(img,(WIDTH/12.5,HEIGHT/12)))
    def run(self):
        if curTime-self.pivotTime>= self.duration:
            self.velocity=random.uniform(3,3.5)
            self.pivotTime=curTime
        self.x += self.velocity 
    def runAnimation(self,ok):
        if self.curSprite>3:
            self.curSprite=0
        if ok:
            self.curSprite+=0.4
        draw(self.img[int(self.curSprite)],self.x,self.y)
    def resize(self):
        w = screen.get_width()
        h = screen.get_height()
        for i in range(4):
            self.img[i] = pygame.transform.scale(self.img[i],(w/12.5,h/12))
        self.velocity = w * self.velocity / self.oldWidth
        self.oldWidth = screen.get_width()
        self.y=h/self.ratio    