from pygame_functions import *
import math, random, time, pickle

screenSize(1000,1000)
setBackgroundColour("black")


class Creature:
    def __init__(self,x,y,image,  size):
        self.x = x
        self.y = y
        self.speed = random.randint(5,15)
        self.angle = random.randint(1,360)
        self.size = size   # size is a percentage of the full size image
        self.sprite = makeSprite(image)
        moveSprite(self.sprite,self.x,self.y,centre=True)
        transformSprite(self.sprite, self.angle, self.size/100)
        showSprite(self.sprite)
    
    def move(self):
        xspeed = self.speed * math.cos(self.angle/180*math.pi)
        yspeed = self.speed * math.sin(self.angle/180*math.pi)
        self.x = (self.x + xspeed) %1000  
        self.y = (self.y + yspeed) %1000 
        moveSprite(self.sprite, self.x, self.y, centre = True)

Class Player(Creature):


setAutoUpdate(False)


creatures = []
for i in range(10):
    c1 = creatures.append(Creature(random.randint(0,1000),random.randint(0,1000), "enemyPlayer.png", random.randint(100,1000)))


while True:
    for c in creatures:
        c.move()
    updateDisplay()
    tick(50)

updateDisplay()
        
endWait()
