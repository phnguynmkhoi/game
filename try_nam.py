# from pygame.locals import *
from turtle import width
import pygame,sys
import random
import time
import math
from testAi import responseChat
pygame.init()
def play(screen,mapSelected,pickedCar,transSelected,mode,manhinh,playerName):
    pygame.mixer.music.load('sounds/backgroundmusic.wav')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    color={0:"red", 1:"blue", 2:"yellow", 3:"green", 4:"pink"}
    #System Time
    curTime=0
    pivotTime=pygame.time.get_ticks()
    iCountdown=0
    rank=0
    listRank=[]
    finished=[0,0,0,0,0]
    picked = -1
    rotateChecked = 0
    rotateCount = 0
    #set screen
    WIDTH=1024
    HEIGHT=534
    screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
    #set caption and icon and image and font
    pygame.display.set_caption("Game cua nha cai den tu Chau Au")
    icon = pygame.image.load('img/mics/car.png')
    pygame.display.set_icon(icon)
    arrow = pygame.image.load('img/mics/arrow.png')
    font = pygame.font.Font('./font/Audiowide-Regular.ttf',int(screen.get_width()/6.667))
    fontRank = pygame.font.Font('./font/Audiowide-Regular.ttf',int(screen.get_width()/16))
    fontChat = pygame.font.Font('./font/Arial.ttf',int(screen.get_width()/69))
    fontName = pygame.font.Font('./font/Arial.ttf',int(screen.get_width()/70))
    fontResponse = pygame.font.Font('./font/Arial.ttf',int(screen.get_width()/15))
    #Mystery Box
    mysbox=[] 
    for i in range(4):
        img=pygame.image.load(f"img/mics/mysterybox_{i}.png")
        img=pygame.transform.scale(img,(WIDTH/25,HEIGHT/20))
        mysbox.append(img)
    first_velocity = 3
    second_velocity = 4
    oldWidth = screen.get_width()
    oldHeight = screen.get_height()
    #Countdown
    countdownbg=pygame.transform.scale(pygame.image.load("img/mics/testbg.png"),(screen.get_width(),screen.get_height()/2)).convert()
    countdownbg.set_alpha(100)
    countdown=[]
    countdown.append(-1)
    bgwin=[]
    bgwin.append(pygame.transform.scale(pygame.image.load("img/celebrate/bg1.jpg"),(screen.get_width(),screen.get_height())))
    bgwin.append(pygame.transform.scale(pygame.image.load("img/celebrate/bgwin.png"),(screen.get_width(),screen.get_height())))
    #End
    rankImg=[]
    for i in range(5):
        rankImg.append(fontRank.render(f"{i+1}",True,(51, 204, 204)))
    for i in range(5):
        rankImg[i] = pygame.transform.scale(rankImg[i],(screen.get_width()/25,screen.get_height()/10))
    for i in range(3,0,-1):
        countdown.append(pygame.image.load(f"img/mics/{i}.png"))
    countdown.append(font.render(("Goooo!"),True,(51, 204, 204)))
    #Trophy
    prize=[]
    prize.append(pygame.transform.scale(pygame.image.load("img/celebrate/first.png"),(WIDTH/15,HEIGHT/9)))
    prize.append(pygame.transform.scale(pygame.image.load("img/celebrate/second.png"),(WIDTH/15,HEIGHT/9)))
    prize.append(pygame.transform.scale(pygame.image.load("img/celebrate/third.png"),(WIDTH/15,HEIGHT/9)))
    #chat
    chatList = ["VN vô địch","Cầm sổ đỏ rồi","đừng thua nữa bán xe rồi","MU vô hang","Arg vô địch","non quá","xin cái tuổi","ez game","nhảy cầu thôi","tạm biệt mọi người","cược nhầm xe rồi","đau lưng quá","nhà mình còn gì đâu"]
    botList = ["Khoi","Nam Android","Huy","Tung","Uong Nam"]
    vowel=["á","à","ả","ã","ạ","ă","ắ","ằ","ẳ","ẵ","ặ","â","ấ","ầ","ẩ","ẫ","ậ","é","è","ẻ","ẽ","ẹ","ê","ế","ề","ể","ễ","ệ","ó","ò","ỏ","õ","ọ","ô","ố","ồ","ổ","ỗ","ộ","ơ","ớ","ờ","ở","ỡ","ợ","í","ì","ỉ","ĩ","ị","ú","ù","ủ","ũ","ụ","ư","ứ","ừ","ử","ữ","ự","ý","ỳ","ỷ","ỹ","ỵ","đ"]


    #Sound
    pickedSound= pygame.mixer.Sound('Music/ding2.wav')
    windSound= pygame.mixer.Sound('Music/wind/Wind.ogg')
    thunderSound = pygame.mixer.Sound('Music/thunderclap.ogg')
    chatPredict=[]

    class CHAT:
        def __init__(self):
            self.chatScript=[]
            self.chatTime=0
            self.inputText=""
            self.onDisplay=True
            self.activeInput=True
        def randomChatScript(self):
            randomChat = chatList[random.randint(0,12)]
            randomName = botList[random.randint(0,4)]
            self.chatScript.append(fontChat.render(randomName+": "+randomChat,True,(115,147,179)))
        def runChat(self):
            self.chatTime+=50
            if self.chatTime%5000==0:
                self.randomChatScript()
            n=4
            for i in range(n):
                j=len(self.chatScript)-i-1
                if j>=0:
                    draw(self.chatScript[j],screen.get_width()/60,screen.get_height()/30+(n-i)*screen.get_height()/30)
                self.displayInputChat()
        def displayInputChat(self):
            surf=fontChat.render("Chat: "+ self.inputText,True,(115,147,179))
            draw(surf,screen.get_width()/60,screen.get_height()/30+5*screen.get_height()/30)
        def pubChat(self):
            if self.inputText!="":
                surf=fontChat.render("You: "+self.inputText,True,(115,147,179))
                self.chatScript.append(surf)
                chatPredict.append([self.inputText,0])
                self.inputText=""
    class STOREEFFECT:
        def __init__(self,buffSpeed,buffEffect,removeEffect,mysteryBox):
            self.buffSpeed = buffSpeed
            self.buffEffect = buffEffect
            self.removeEffect = removeEffect
            self.mysteryBox = mysteryBox
            self.count = 0
            self.curTime = 0
        def display(self):
            effectDisplay = []
            if self.buffSpeed == 1:
                img = pygame.image.load("./Image/Store/eff/1.png")
                effectDisplay.append(pygame.transform.scale(img,(screen.get_width()/18,screen.get_height()/10)))
            if self.buffEffect == 1:
                img = pygame.image.load("./Image/Store/eff/2.png")
                effectDisplay.append(pygame.transform.scale(img,(screen.get_width()/18,screen.get_height()/10)))
            if self.removeEffect == 1:
                img = pygame.image.load("./Image/Store/eff/3.png")
                effectDisplay.append(pygame.transform.scale(img,(screen.get_width()/18,screen.get_height()/10)))
            if self.mysteryBox == 1:
                img = pygame.image.load("./Image/Store/eff/4.png")
                effectDisplay.append(pygame.transform.scale(img,(screen.get_width()/18,screen.get_height()/10)))
            for i in range(len(effectDisplay)):
                draw(effectDisplay[i],screen.get_width()-screen.get_width()/15*(i+1),screen.get_height()/45)
        def drawRemove(self):
            self.curTime+=1
            if self.curTime<=80 and car[carSelected].curRound == car[pickedCar].curRound:
                draw(pygame.transform.scale(pygame.image.load("./Image/Store/eff/3.png"),(screen.get_width()/30,screen.get_height()/20)),car[pickedCar].x,car[pickedCar].y-screen.get_height()/20)
    #CHAT
    chat = CHAT()
    #function for GAME
    def draw(player_car,x,y):
        screen.blit(player_car,(x, y))
    def isCollide(a,b,x,y):
        return (math.sqrt((a-x)*(a-x)+(b-y)*(b-y))<screen.get_width()/12.5)
    def distance(a,b,x,y):
        return math.sqrt((a-x)*(a-x)+(b-y)*(b-y))
    def resizemysbox(i):
        img = mysbox[i] 
        return pygame.transform.scale(img,(screen.get_width()/25,screen.get_height()/20))
    def rand():
        a=random.randint(0,3)
        b=random.randint(0,3)
        while a==b:
            b=random.randint(0,3)
        return [a,b]
    class ITEM :
        def __init__(self,y,velocity,img):
            self.img = mysbox
            self.curBox=0
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
            if i == pickedCar and store.buffEffect == 1:
                car[pickedCar].velocity = car[pickedCar].velocity * 1.5
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
                if idx == pickedCar and store.buffEffect == 1:
                    car[pickedCar].velocity = car[pickedCar].velocity / 1.5
            
        def setLaser(self):
            self.curSprite=0    
            self.laser=1

        def runLaser(self,idx):
            self.curSprite+=0.10
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
            car[idx].x+=screen.get_width()/6
            if idx == pickedCar and buffEffect == 1:
                car[idx].x*=1.2
            car[idx].y=-1000
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
                img = pygame.image.load(f"./img/mics/nitro_{j}.png")
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
        def __init__(self,img, start,end,win='') :
            self.img=pygame.transform.scale(img,(screen.get_width(),screen.get_height()))
            self.winBackground=win
            self.start=start
            self.end=end
            self.car=[]

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
            if rank==5:
                self.x += WIDTH/400
                return
            if curTime-self.pivotTime>= self.duration and self.velocity!=0:
                tmp=random.uniform(self.velocity-0.3,second_velocity)
                if tmp>=self.velocity:
                    self.curSpriteSmoke=0
                    self.velocity=tmp
                self.pivotTime=curTime
                self.smokeX=self.x-screen.get_width()/33.34
            self.x+=self.velocity
        def runAnimation(self,ok):
            if ok:
                self.curSpriteWheel+=0.4
            if self.curSpriteWheel>=len(self.spriteWheel):
                self.curSpriteWheel=0
            draw(self.spriteWheel[int(self.curSpriteWheel)] ,self.x,self.y)
            # if rank==5:
            #     return
            self.curSpriteSmoke+=0.2
            if self.curSpriteSmoke<len(self.spriteSmoke) :
                if int(self.curSpriteSmoke)<=5  :
                    self.smokeX=self.x-screen.get_width()/30
                if  self.x>self.smokeX:
                    draw(self.spriteSmoke[int(self.curSpriteSmoke)],self.smokeX,self.y+screen.get_height()/28)

        def resize(self):
            w = screen.get_width()
            h = screen.get_height()
            for i in range(len(self.spriteWheel)):
                self.spriteWheel[i] = pygame.transform.scale(self.spriteWheel[i],(w/12.5,h/12))
            global oldWidth,first_velocity,second_velocity
            self.x = self.x * screen.get_width() / oldWidth
            self.y=h/self.ratio

        def bigger(self):
            for i in range(len(self.spriteWheel)):
                self.spriteWheel[i]=pygame.transform.scale( self.spriteWheel[i],(WIDTH/9,HEIGHT/7))
    class CELEBRATE:
        def __init__(self,x,y) :
            self.crowdImg=[]
            self.crowdX,self.crowdY=x,y
            self.curSprite=0
        def runAnimation(self):
            for i in range (len(self.crowdImg)):
                self.curSprite+=0.05
                draw(self.crowdImg[int(self.curSprite)%len(self.crowdImg)],self.crowdX,self.crowdY)
        def resize(self):
            self.crowdX = self.crowdX * screen.get_width() / oldWidth
            self.crowdY = self.crowdY * screen.get_height() / oldHeight
            for i in range(len(self.crowdImg)):
                self.crowdImg[i] = pygame.transform.scale(self.crowdImg[i],(screen.get_width()/3,screen.get_height()/5))
    #Background INITIALIZATION
    mode=2
    bg=[]
    NumRound=mode#Số round của game (2->4)
    mapp=['city','desert','galaxy','painting','sea']
    for i in range(5):
        bg.append([])
        for j in range(4):
            start,end=0,screen.get_width()  
            img=(f"img/background-levels/background-{mapp[i]}-{j}.png")
            bg[i].append(BACKGROUND(pygame.image.load(img),start,end))
    # Car INITIALIZATION
    car=[]
    transportation={
        0:("formula ones",4,9,"smoke"), # loai phuong tien/so sprite phuong tien/ so sprite animation hieu ung/ten hieu ung
        1:("spaceship",1,4,"fire"),
        2:("trucks",4,9,"smoke"),
        3:("scooters",3,9,"smoke"),
        4:("motorcycles",3,9,"smoke")
    }
    carName = ["Khoi","Nam","Huy","Tung","Android"]
    transSelected=0# Change Transportation here
    pickedCar = 1
    mapSelected = 4
    r=[2.28,1.83,1.5,1.27,1.12] # ratio cho vo 1 mang de initialize

    for i in range (5):
        trans= transportation[transSelected]
        car.append(CAR(HEIGHT,r[i], random.uniform(first_velocity,second_velocity), 0))
        if transSelected == 4 or transSelected == 1:
            for j in range(trans[1]): # Add animation
                img=pygame.image.load(f"img/{trans[0]}/{j}_{color[i]}.png")
                img =pygame.transform.scale(img,(WIDTH/12.5,HEIGHT/12))
                car[i].spriteWheel.append(img)
        else:
            for j in range(trans[1]-1,0,-1): # Add animation
                img=pygame.image.load(f"img/{trans[0]}/{j}_{color[i]}.png")
                img =pygame.transform.scale(img,(WIDTH/12.5,HEIGHT/12))
                car[i].spriteWheel.append(img)
        for j in range(trans[2]):
            img=pygame.transform.scale(pygame.image.load(f"./img/mics/{trans[3]}_{j}.png"),(screen.get_width()/20,screen.get_height()/20))
            car[i].spriteSmoke.append(img)

    # Item INITIALIZATION
    item=[]
    for i in range(5):
        item.append(ITEM(car[i].y+int(screen.get_height()/50),car[i].velocity,mysbox))
    for i in range(5):
        for j in range(4):
            img = pygame.image.load(f"img/mics/stun_{j}.png")
            img = pygame.transform.scale(img,(screen.get_width()/25,screen.get_height()/20))
            item[i].spriteStun.append(img)
        for j in range(8):
            img = pygame.image.load(f"img/mics/nitro_{j}.png")
            img = pygame.transform.scale(img,(screen.get_width()/15,screen.get_height()/20))
            item[i].spriteBoost.append(img)
        for j in range (1):
            img=pygame.image.load(f"img/mics/turtle.png")
            img = pygame.transform.scale(img, (screen.get_width()/18,screen.get_height()/15))
            item[i].spriteSlow.append(img)
        for j in range(8):
            img=pygame.image.load(f"img/mics/portal_{j}.png")
            img = pygame.transform.scale(img,(screen.get_width()/18,screen.get_height()/8))
            item[i].spriteWin.append(img)
        for j in range(5):
            img=pygame.image.load(f"img/mics/flash_{j}.png")
            img = pygame.transform.scale(img,(screen.get_width()/7,screen.get_height()/7))
            item[i].spriteFlash.append(img)
        for j in range(8):
            img=pygame.image.load(f"img/mics/portal_lose_{j}.png")
            img = pygame.transform.scale(img,(screen.get_width()/18,screen.get_height()/8))
            item[i].spriteLose.append(img)
        for j in range(6):
            img=pygame.image.load(f"img/mics/flip_{j}.png")
            img = pygame.transform.scale(img, (screen.get_width()/20,screen.get_height()/5))
            item[i].spriteFlip.append(img)
        for j in range(5):
            img=pygame.image.load(f"img/mics/lightning_{j}.png")
            img = pygame.transform.scale(img,(screen.get_width()/14,screen.get_height()))
            item[i].spriteLaser.append(img)

    #store item initialization
    buffSpeed = 0
    buffEffect = 0
    removeEffect = 0
    mysteryBox = 1
    runRemoveEffect = 0
    countdownChecked = 0
    useMys = 0
    store = STOREEFFECT(buffSpeed, buffEffect, removeEffect, mysteryBox)
    if buffSpeed == 1:
        car[pickedCar].velocity*=1.2

    #when choose the right car
    text_lose = "YOU LOSE"
    text_win = "YOU WIN"

    #Crowd INITIALIZATION
    crowd=[]
    for i in range(5):
        crowd.append(CELEBRATE(10+i*screen.get_width()/5,screen.get_height()/3))
        for j in range(2):
            img=pygame.image.load(f"img/celebrate/crowd{i%2}_{j}.png")
            img=pygame.transform.scale(img,(screen.get_width()/3,screen.get_height()/5))
            crowd[i].crowdImg.append(img)

    #######
    #######

    chatResponse=[]
    chatResponse={-1:"Cay không",0:"Trung lập",1:"Vui"}

    #game Loop
    clock = pygame.time.Clock()
    fps = 60

    #Initalize
    r=0
    carSelected=0 
    #mapSelected=#Change map here
    pressed=0
    checkMenu=0
    happiness=0
    for i in range (5):
        bg[mapSelected][r].car.append(i)
        car[i].x=bg[mapSelected][r].start
        car[i].curRound=r
    #GAME
    #test game
    #for i in range(5):
    #    car[i].velocity = 1000
    #player car
    nameDisplay = []
    for i in range(5):
        if i == pickedCar:
            nameDisplay.append(fontName.render(playerName,True,(0,255,255)))
        else:
            nameDisplay.append(fontName.render(carName[i],True,(255,255,255)))
    #set cursor
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    chatWidthMin = screen.get_width()/18
    chatHeightMin = screen.get_height()/4.9
    chatWidthMax = screen.get_width()/18+screen.get_width()/5
    chatHeightMax = screen.get_height()/4.9+screen.get_height()/35
    chatChecked = 0
    running = True
    while running:
        if curTime-pivotTime>100000:
            running=False
        curTime=pygame.time.get_ticks()
        clock.tick(fps)        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            #Nhap text                
                        
            if event.type == pygame.MOUSEBUTTONUP:
                if (pygame.mouse.get_pos()[0]>=chatWidthMin) and (pygame.mouse.get_pos()[0]<=chatWidthMax) and (pygame.mouse.get_pos()[1]>=chatHeightMin) and (pygame.mouse.get_pos()[1]<=chatHeightMax):
                    chat.activeInput = 1
                else:
                    chat.activeInput = 0
            if chat.activeInput == 1:
                ok=0
                if event.type==pygame.KEYDOWN:
                    #print (event)
                    for c in vowel:
                        if event.unicode==c:
                            chat.inputText=chat.inputText[:-1]
                            chat.inputText+=event.unicode
                            ok=1
                    if ok==0:
                        if event.key==pygame.K_BACKSPACE:
                            chat.inputText=chat.inputText[:-1]
                        elif event.key==pygame.K_RETURN:
                            chat.pubChat()
                        else:
                            chat.inputText+= event.unicode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if rank == 5:
                        if  checkMenu==1:
                            running=False
                        checkMenu=1
                if event.key == pygame.K_SPACE and store.mysteryBox == 1 and countdownChecked == 1:
                    useMys = 1
                    store.mysteryBox = 0
            #Het phan nhap Text
            if event.type == pygame.KEYDOWN and pressed==0:
                pressed=1
                if event.key==pygame.K_F1:
                    carSelected=0
                elif event.key==pygame.K_F2:
                    carSelected=1
                elif event.key==pygame.K_F3:
                    carSelected=2
                elif event.key==pygame.K_F4:
                    carSelected=3
                elif event.key==pygame.K_F5:
                    carSelected=4
                else: 
                    pressed=0
            if event.type == pygame.KEYUP and pressed:
                pressed=0
            #resize screen
            if event.type == pygame.VIDEORESIZE:
                
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                for i in range (4):
                    img=(f"img/background-levels/background-{mapp[mapSelected]}-{i}.png")
                    bg[mapSelected][i].img = pygame.transform.scale(pygame.image.load(img),(screen.get_width(),screen.get_height()))
                    bg[mapSelected][i].end = screen.get_width()
                fps = fps * (screen.get_width() / oldWidth + screen.get_height() / oldHeight)
                first_velocity = first_velocity * screen.get_width() / oldWidth
                second_velocity = second_velocity * screen.get_width() / oldWidth
                for i in range(5):
                    car[i].resize()
                    car[i].velocity = car[i].velocity * screen.get_width() / oldWidth
                    item[i].y=car[i].y + int(screen.get_height()/50)
                    
                    #resize smoke
                    for j in range(trans[2]):
                        car[i].spriteSmoke[j] = pygame.transform.scale(car[i].spriteSmoke[j],(screen.get_width()/20,screen.get_height()/20))
                    item[i].resize(i)
                    for i in range(4):
                        mysbox[i] = resizemysbox(i)
                    item[i].velocity = car[i].velocity
                #resize countdown
                countdownbg=pygame.transform.scale(pygame.image.load("img/mics/testbg.png"),(screen.get_width(),screen.get_height()/2)).convert()
                countdownbg.set_alpha(200)    
                #resize rank
                for i in range(5):
                    rankImg[i] = pygame.transform.scale(rankImg[i],(screen.get_width()/25,screen.get_height()/10))
                bgwin[0] = pygame.transform.scale(bgwin[0],(screen.get_width(),screen.get_height()))
                bgwin[1] = pygame.transform.scale(bgwin[1],(screen.get_width(),screen.get_height()))
                pygame.transform.scale(pygame.image.load("img/celebrate/first.png"),(screen.get_width()/15,screen.get_height()/9))
                pygame.transform.scale(pygame.image.load("img/celebrate/second.png"),(screen.get_width()/15,screen.get_height()/9))
                pygame.transform.scale(pygame.image.load("img/celebrate/third.png"),(screen.get_width()/15,screen.get_height()/9))
                for i in range(len(crowd)):
                    crowd[i].resize()
                oldWidth = screen.get_width()
                oldHeight = screen.get_height()
        # Celebrate
        
        if rank==5 :
            if rotateChecked == 0:
                for i in range(5):
                    if finished[i] == 1:
                        winTrans = transportation[transSelected]
                        img = pygame.image.load(f"img/{winTrans[0]}/0_{color[i]}.png")
                        img = pygame.transform.scale(img,(screen.get_width()/12.5,screen.get_height()/12))
                        img = pygame.transform.rotate(img,2*rotateCount)
                        car[i].spriteWheel[0] = img
                rotateCount+=1
                if rotateCount >= 5:
                    rotateChecked = 1
            else:
                for i in range(5):
                    if finished[i] == 1:
                        winTrans = transportation[transSelected]
                        img = pygame.image.load(f"img/{winTrans[0]}/0_{color[i]}.png")
                        img = pygame.transform.scale(img,(screen.get_width()/12.5,screen.get_height()/12))
                        img = pygame.transform.rotate(img,2*rotateCount)
                        car[i].spriteWheel[0] = img
                rotateCount-=1
                if rotateCount <= -5:
                    rotateChecked = 0
            if curTime-pivotTime>2000:
                for i in range(len(bgwin)):
                    draw(bgwin[i],0,0)
                for i in range(len(crowd)):
                    crowd[i].runAnimation()
                for i in range(5):
                    car[i].ratio=1.7
                    car[i].bigger()
                    car[i].run()
                    draw(car[i].spriteWheel[0],car[i].x,screen.get_height()/car[i].ratio)
                    if finished[i]<=3:
                        draw(prize[finished[i]-1],car[i].x+screen.get_width()/300,screen.get_height()/2)
                if checkMenu==1:
                    draw(countdownbg,0,(screen.get_height()-screen.get_height()/2)/2)
                    draw(happiness,(screen.get_width()-happiness.get_width())/2,(screen.get_height()-happiness.get_height())/2)
                if finished[pickedCar]==1:
                    if curTime%1000<333:
                        textInside = fontRank.render(text_win,True,(220,20,60))
                    elif curTime%1000<=667:
                        textInside = fontRank.render(text_win,True,(255,255,255))
                    else: 
                        textInside = fontRank.render(text_win,True,(0,0,0))
                    screen.blit(pygame.transform.scale(textInside,(screen.get_width()/4,screen.get_height()/5)),(screen.get_width()/2.7,screen.get_height()/6))
                else:
                    if curTime%1000<333:
                        textInside = fontRank.render(text_lose,True,(220,20,60))
                    elif curTime%1000<=667:
                        textInside = fontRank.render(text_lose,True,(255,255,255))
                    else: 
                        textInside = fontRank.render(text_lose,True,(0,0,0))
                    screen.blit(pygame.transform.scale(textInside,(screen.get_width()/4,screen.get_height()/5)),(screen.get_width()/2.7,screen.get_height()/6))
                 
            else :
                happiness= fontResponse.render(chatResponse[responseChat(chatPredict)],True,(204, 51, 153))
                for i in range(5):
                    car[i].x=-screen.get_width()/10-finished[i]*screen.get_width()/8

            pygame.display.update()
            continue
        
        draw(bg[mapSelected][car[carSelected].curRound].img,0,0)   
        #display store effect
        store.display()
        if runRemoveEffect == 1:
            store.drawRemove()
            
        for i in range(5):
            if car[i].curRound == car[carSelected].curRound and (i!=carSelected or pressed == 0):
                draw(nameDisplay[i],car[i].x+screen.get_width()/30,car[i].y-screen.get_height()/35)
        #draw 5 car
        for i in bg[mapSelected][car[carSelected].curRound].car:
            if car[i].x <= bg[mapSelected][car[carSelected].curRound].end: # check finished 
                car[i].runAnimation(1)
            else:
                car[i].runAnimation(0)
        #draw item
        for i in range(5):
            for j in range (2):
                if item[i].appRound[j] == car[carSelected].curRound and item[i].visible[j]==1:
                    draw(item[i].img[int(item[i].curBox)%4],item[i].x[j],item[i].y)
                    item[i].curBox+=0.08
        #CHAT
        chat.runChat()
        if curTime-pivotTime<6000 and rank==0:
            draw(countdownbg,0,(screen.get_height()-screen.get_height()/2)/2)
            iCountdown=int((curTime-pivotTime)/1000)-1
            if iCountdown>0:
                draw(countdown[iCountdown],
                (screen.get_width()-countdown[iCountdown].get_width())/2,(screen.get_height()-screen.get_height()/5)/2)
            pygame.display.update()
            continue
        else: 
            countdownChecked = 1
            
        #items influence
        for i in range(5):
            #Slower
            if item[i].slow==1:
                item[i].runSlow(i)
            #Faster
            if item[i].boost==1:
                item[i].runFaster(i)
            #Win
            if item[i].openPortal==1:
                # print (i)
                item[i].runWin(i)
            if item[i].openPortal==2:
                item[i].runLose(i)
            #Flash
            if car[i].y<0 :
                item[i].runFlash(i)
            #runStun
            if item[i].laser==1 :
                item[i].runLaser(i)
            if item[i].laser==2:
                if car[i].velocity == 0:
                    item[i].runStun(i)
            #Flip
            if item[i].checkFlip==1:
                item[i].runFlip(i)

            if item[i].checkFlip == 0 and (item[i].countFlip % 2 == 1):
                for j in range (len(car[i].spriteWheel)):
                    car[i].spriteWheel[j] = pygame.transform.flip(car[i].spriteWheel[j],True,False)
                item[i].countFlip = 0
        #Check collision
        for i in range (5):
            for j in range(2):
                if (item[i].appRound[j] == car[i].curRound and isCollide(car[i].x,car[i].y,item[i].x[j],item[i].y) and item[i].visible[j]) or (useMys == 1 and i == pickedCar):
                    if i != pickedCar or useMys == 0:
                        item[i].visible[j]=0
                    if i == pickedCar and useMys == 1:
                        useMys = 0
                    picked=random.randint(0,99)
                    #picked =26
                    if picked < 25:
                        if i == pickedCar:
                            if store.removeEffect == 0:
                                item[i].slower(i)
                            else:
                                store.removeEffect = 0
                                runRemoveEffect = 1
                        else:
                            item[i].slower(i)
                    elif picked < 55:
                        item[i].faster(i)
                    elif picked < 70:
                        if i == pickedCar:
                            if store.removeEffect == 0:
                                item[i].flip()
                                windSound.play()
                            else:
                                store.removeEffect = 0
                                runRemoveEffect = 1
                        else:
                            item[i].flip()
                            windSound.play()
                    elif picked == 71:
                        item[i].win(i)
                        item[i].portalX=car[i].x+screen.get_width()/5
                    elif picked<=79:
                        if i == pickedCar:
                            if store.removeEffect == 0:
                                item[i].lose(i)
                                item[i].portalX=car[i].x+screen.get_width()/5
                            else:
                                store.removeEffect = 0
                                runRemoveEffect = 1
                        else:
                            item[i].lose(i)
                            item[i].portalX=car[i].x+screen.get_width()/5
                    elif picked<=91 :
                        item[i].flash(i)
                    else:
                        if i == pickedCar:
                            if store.removeEffect == 0:
                                item[i].setLaser()
                                thunderSound.play()
                            else:
                                store.removeEffect = 0
                                runRemoveEffect = 1
                        else:
                            item[i].setLaser()
                            thunderSound.play()

        if pressed ==1:
            for i in bg[mapSelected][car[carSelected].curRound].car:
                if i==carSelected :
                    draw(arrow,car[i].x+screen.get_width()/100,car[i].y-screen.get_height()/13.4)
        #check if the car have finish the race
        for i in range (5):
            if car[i].x<=bg[mapSelected][car[i].curRound].end+100 and rank<5:
                car[i].run()
            elif car[i].curRound<3: 
                bg[mapSelected][car[i].curRound].car.remove(i)
                if car[i].curRound==0:
                    if NumRound==2:
                        car[i].curRound+=2
                    if NumRound==3:
                        car[i].curRound+=1
                
                car[i].curRound+=1
                bg[mapSelected][car[i].curRound].car.append(i)
                car[i].x=bg[mapSelected][car[i].curRound].start-(screen.get_width()/10)
            else: 
                if finished[i]==0:
                    finished[i]=rank+1
                    listRank.append((rankImg[rank],car[i].ratio))
                    rank+=1
                    pivotTime=curTime
        pygame.display.update()

    pygame.quit()
play(0,0,0,0,0,0,"NotTun")