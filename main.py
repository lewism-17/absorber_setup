from pygame_functions import *
import math, random, time, pickle

screenSize(1800,1000)
setBackgroundColour("black")
setAutoUpdate(False)

die = makeSound("thump.mp3")

class Creature:
    def __init__(self,x,y,image,  size):
        self.x = x
        self.y = y
        self.speed = random.randint(4,8)
        self.angle = random.randint(1,360)
        
        self.size = size   # size is a percentage of the full size image
        self.sprite = makeSprite(image)
        moveSprite(self.sprite,self.x,self.y,centre=True)
        transformSprite(self.sprite, self.angle, self.size/100)
        showSprite(self.sprite)

    def move(self):
        xspeed = self.speed * math.cos(self.angle/180*math.pi)
        yspeed = self.speed * math.sin(self.angle/180*math.pi)
        # change the x position and y position of this creature
        self.x = (self.x + xspeed) % 1800
        self.y = (self.y + yspeed) % 1000
        # move the sprite
        moveSprite(self.sprite,   self.x, self.y, centre=True)


class Player(Creature):
    def move(self, creatures):
        # work out the angle from the player to the mouse
        dx = mouseX() - self.x
        dy = mouseY() - self.y
        dist = math.sqrt(dx**2 + dy**2)
        self.speed = dist /200 * 10
        self.angle = math.degrees(math.atan2(dy, dx))
        transformSprite(self.sprite, self.angle, self.size/100)
        super().move()
        for c in creatures:
            if touching(self.sprite, c.sprite):
                if self.size > c.size:
                    print("Nom")
                    creatures.remove(c)
                    hideSprite(c.sprite)
                    self.size += 5
                elif self.size < c.size:
                    playSound(die)


creatures= [ ]
for i in range(10):
    creatures.append(Creature(random.randint(0,1000),random.randint(0,1000), "enemy.png", random.randint(5,50)))       

p = Player(500,500,"player.png",20)

while True:
    for c in creatures:
        c.move()
    p.move(creatures)
    updateDisplay()
    tick(50)
endWait()
