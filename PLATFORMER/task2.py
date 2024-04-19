from pygame import*
from level import level
import time
SIZE=(1280,720)
win=display.set_mode(SIZE)
display.set_caption("Blockada")

background="./images/bgr.png"
img_coin="./images/coin.png"
img_door="./images/door.png"
img_key="./images/key.png"
img_chest_open="./images/cst_open.png"
img_chest_close="./images/cst_close.png"
img_cyborg="./images/cyborg.png"
img_stair="./images/stair.png"
img_port="./images/portal.png"
img_platform="./images/platform.png"
img_nothing="./images/nothing.png"
img_power="./images/mana.png"

bg=transform.scale(image.load(background),SIZE)

class Settings(sprite.Sprite):
    def __init__(self,x,y,w,h,speed,img,*args,**kw):
        super().__init__()
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.speed=speed
        self.image=transform.scale(image.load(img),(w,h))
        self.rect=self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y

    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Player(Settings):
    def controll(self):
        keys=key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x-=self.speed
        if keys[K_RIGHT]:
            self.rect.x+=self.speed
        if keys[K_a]:
            self.rect.x-=self.speed
        if keys[K_d]:
            self.rect.x+=self.speed
        if(keys[K_w]):
            self.rect.y-=self.speed
        if(keys[K_s]):
            self.rect.y+=self.speed

class Camera():
    def __init__(self, camera_func, w,h):
        self.camera_func = camera_func
        self.state = Rect(0,0,w,h)

    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_config(camera, target_rect):
    l,t,_,_ = target_rect
    _,_,w,h = camera
    l,t = -l +W/2, -t+ H/2
    l = min(0,1)
    l = max(-(camera.width - W), l)
    t = max(-(camera.height - H), t)
    t = min(0, t)
    return Rect(l,t,w,h)
        


player=Player(x=0,y=0,speed=10,w=100,h=100,img="./images/sprite1.png")
isGame=True
blocks_r = []
blocks_l = []
coins = []
staits = []
platforms = []

items = sprite.Group()

#TODO GAME
win.blit(bg,(0,0))
x = y = 0
for r in level:
        for c in r:
            if c == 'r':
                r1 = Settings(x,y,40,40,0,img_nothing)
                r1.reset()
            if c == 'l':
                r2 = Settings(x,y,40,40,0,img_nothing)
                r2.reset()
            if c == '/':
                r3 = Settings(x,y-40,40,180,0,img_stair)
                r3.reset()
            if c == '°':
                r4 = Settings(x,y,40,40,0,img_coin)
                r4.reset()
            if c =='-':
                r5 = Settings(x,y,40,40,0,img_platform)
                r5.reset()
            x+=40
        y+=40
        x=0
    
while isGame:
    
    for e in event.get():
        if e.type==QUIT:
            isGame=False
    #player.controll()
    #player.reset()
    #time.sleep(0.1)
    display.update()