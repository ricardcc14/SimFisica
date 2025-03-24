import pygame
import numpy as np
import Box2D as b2
import utils
import time

class Bird:
    def __init__(self, world:b2.b2World, x:float, y:float, radius:float, images:list[pygame.Surface]):
        self.radius = radius
        self.images = images

        self.timer = 0
        self.collisionTime = 3
        self.deathTime = 1
        self.prevSec = 0

        self.collided = False
        self.isRemoved = False
        self.currentStatus = 0 #0 is alive, 1 is collided 2 is toDestroy

        bodydf = b2.b2BodyDef()
        bodydf.position = utils.pixelToWorld(x, y)
        bodydf.type = b2.b2_dynamicBody
        bodydf.userData = self
        self.body:b2.b2Body = world.CreateBody(bodydf)

        circleshape = b2.b2CircleShape()
        circleshape.radius = utils.pixelToWorld(radius)
        fd = b2.b2FixtureDef()
        fd.shape=circleshape
        fd.density = 5
        fd.restitution = 0.5
        fd.friction = 0.3
        self.body.CreateFixture(fd)
        pass

    def draw(self, screen:pygame.Surface):
        position:b2.b2Vec2 = utils.worldToPixel(self.body.position.copy())
        position.y = screen.get_height()-position.y

        utils.drawRotatedImage(screen, self.images[self.currentStatus], position, self.radius*2, self.radius*2, self.body.angle)
        pass

    def update(self, world):
        if(self.collided):
            seconds = time.time()
            if(self.timer > self.collisionTime):
                self.currentStatus = 2
                self.setLinearVelocity(0, 0)
                self.setAngularVelocity(0)
                if((seconds-self.prevSec) > self.deathTime): self.destroy(world)
            else:
                self.currentStatus = 1;
                self.timer+=(seconds-self.prevSec);
                self.prevSec = seconds
        pass

    def setLinearVelocity(self, x:float, y:float, scale:float=5):
        self.body.linearVelocity = scale*utils.pixelToWorld(x, y)

    def setAngularVelocity(self, a:float):
        self.body.angularVelocity = a

    def birdCollided(self):
        if(not self.collided):
            self.collided = True
            self.prevSec = time.time()
        pass

    def destroy(self, world:b2.b2World):
        world.DestroyBody(self.body)
        self.isRemoved = True 
        pass