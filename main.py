from pygame_functions import *
import math, random, time, pickle

screenSize(1800,1000)
setBackgroundColour("black")
setAutoUpdate(False)

#die = makeSound("thump.mp3")

class Creature:
    def __init__(self,x,y,image,  size):
        self.x = x
        self.y = y
        self.speed = random.randint(4,8)
        self.angle = random.randint(1,360)
        
        self.size = size*3   # size is a percentage of the full size image
        self.sprite = makeSprite(image)
        moveSprite(self.sprite,self.x,self.y,centre=True)
        transformSprite(self.sprite, self.angle, self.size/100)
        showSprite(self.sprite)

    def move(self,player):
        xspeed = self.speed * math.cos(self.angle/180*math.pi)
        yspeed = self.speed * math.sin(self.angle/180*math.pi)
        # change the x position and y position of this creature
        self.x = (self.x + xspeed) % 10000
        self.y = (self.y + yspeed) % 10000
        # move the sprite
        moveSprite(self.sprite,900+(self.x-player.x), 450+(self.y-player.y), centre=True)


class Player(Creature):
    def __init__(self,x,y,image, size): 
        super().__init__(x,y,image,size)
        moveSprite(self.sprite,900,450,centre=True)
    
    def move(self, creatures):
        # work out the angle from the player to the mouse
        dx = mouseX() - 900
        dy = mouseY() - 450
        dist = math.sqrt(dx**2 + dy**2)
        self.speed = dist /200 * 10
        self.angle = math.degrees(math.atan2(dy, dx))
        transformSprite(self.sprite, self.angle, self.size/100)
        xspeed = self.speed * math.cos(self.angle/180*math.pi)
        yspeed = self.speed * math.sin(self.angle/180*math.pi)
        self.x = (self.x + xspeed) % 10000
        self.y = (self.y + yspeed) % 10000
        
        
        for c in creatures:
            if touching(self.sprite, c.sprite):
                if self.size > c.size:
                    print("Nom")
                    creatures.remove(c)
                    hideSprite(c.sprite)
                    self.size += 5
                elif self.size < c.size:
                    return False
        return True


creatures= [ ]
for i in range(300):
    creatures.append(Creature(random.randint(0,10000),random.randint(0,10000), "enemyPlayer.png", random.randint(5,50)))       

p = Player(5000,5000,"Player Monster.gif",20)

def drawBoundary(player):
    clearShapes()
    drawRect(900-player.x, 450-player.y, 10000,10000, (0,0,40),0)
    drawRect(900-player.x, 450-player.y, 10000,10000, (255,255,255),5)


while True:
    for c in creatures:
        c.move(p)
    #if not alive:
     #   break
    p.move(creatures)
    drawBoundary(p)
    updateDisplay()
    tick(50)
endWait()
