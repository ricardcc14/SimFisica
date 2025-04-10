import pygame
import numpy as np
import Box2D as b2
import utils
import time

class Pig:
    def __init__(self, world:b2.b2World, x:float, y:float, radius:float, images:list[pygame.Surface]):
        self.radius = radius
        self.images = images

        self.timer = 0
        self.collisionTime = 3
        self.deathTime = 1
        self.prevSec = 0
        self.impactVelocity = 0
        
        self.VELOCITY_BIRD_KILL = 3
        self.VELOCITY_SURF_KILL = 0
        self.VELOCITY_WALL_KILL = 3

        self.collidedWBird = False
        self.collidedWWall = False
        self.collidedWSurf = False
        self.damageSoundPlayed = False
        self.poofSoundPlayed = False

        self.isRemoved = False
        self.currentStatus = 0 #0 is alive, 1 is dead 2 is toDestroy

        bodydf = b2.b2BodyDef()
        bodydf.position = utils.pixelToWorld(x, y)
        bodydf.type = b2.b2_dynamicBody
        bodydf.userData = self
        self.body:b2.b2Body = world.CreateBody(bodydf)

        circleshape = b2.b2CircleShape()
        circleshape.radius = utils.pixelToWorld(radius)
        fd = b2.b2FixtureDef()
        fd.shape=circleshape
        fd.density = 1
        fd.restitution = 0
        fd.friction = 0.3
        self.body.CreateFixture(fd)
        pass

    def draw(self, screen:pygame.Surface):
        position:b2.b2Vec2 = utils.worldToPixel(self.body.position.copy())
        position.y = screen.get_height()-position.y

        utils.drawRotatedImage(screen, self.images[self.currentStatus], position, self.radius*2, self.radius*2, self.body.angle)
        pass

    def update(self, world):
        seconds = time.time()

        if(self.collidedWBird):
            self.currentStatus = 2

            if (self.damageSoundPlayed == False):   
                sound = pygame.mixer.Sound("assets/ui/music/pig-pop.mp3")
                sound.set_volume(0.3)  
                sound.play()
                self.damageSoundPlayed = True

            self.setLinearVelocity(0, 0)
            self.setAngularVelocity(0)
            if((seconds-self.prevSec) > self.deathTime): self.destroy(world)
        pass

        if(self.collidedWSurf or self.collidedWWall):
            if(self.timer > self.collisionTime):
                self.currentStatus = 2
                self.setLinearVelocity(0, 0)
                self.setAngularVelocity(0)
                if((seconds-self.prevSec) > self.deathTime): self.destroy(world)
                
            else:

                if (self.damageSoundPlayed == False):   
                    sound = pygame.mixer.Sound("assets/ui/music/pig-damage.mp3")
                    sound.set_volume(0.3)  
                    sound.play()
                    self.damageSoundPlayed = True

                if (self.currentStatus != 1):
                    self.currentStatus = 1
                    self.timer+=(seconds-self.prevSec)
                    self.prevSec = seconds



    def pigCollidedWithBird(self, impactVel):
        if(not self.collidedWBird):
            if (impactVel >= self.VELOCITY_BIRD_KILL):
                self.collidedWBird = True
                self.prevSec = time.time()
                self.impactVelocity = impactVel
                return True
            else:
                return False
        pass

    def pigCollidedWithSurf(self, impactVel):
        if(not self.collidedWSurf):
            if (impactVel >= self.VELOCITY_SURF_KILL):
                self.collidedWSurf = True
                self.prevSec = time.time()
                self.impactVelocity = impactVel
                return True
            else:
                return False
    pass

    def pigCollidedWithWall(self, impactVel1, impactVel2):
       
        impactVel = max(impactVel1, impactVel2)

        if(not self.collidedWSurf):
            if (impactVel >= self.VELOCITY_WALL_KILL):
                self.collidedWWall = True
                self.prevSec = time.time()
                self.impactVelocity = impactVel
                return True
            else:
                return False
    pass





    def setLinearVelocity(self, x:float, y:float, scale:float=5):
        self.body.linearVelocity = scale*utils.pixelToWorld(x, y)

    def setAngularVelocity(self, a:float):
        self.body.angularVelocity = a

    def getLinearVelocity(self):
        return self.body.linearVelocity

    def destroy(self, world:b2.b2World):
        world.DestroyBody(self.body)
        self.isRemoved = True 
        pass