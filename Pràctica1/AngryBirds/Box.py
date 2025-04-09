import pygame
import Box2D as b2
import utils
import time

class Box:
    def __init__(self, world:b2.b2World, x:float, y:float, w:float, h:float, images:list[pygame.Surface]):
        self.w = w
        self.h = h
        self.images = images

        #self.material = material
        self.collided = False
        self.isRemoved = False
        self.currentStatus = 0 #0 is intact, 1 is collided 2 is 'poof' 3 is toDestroy
        self.timer = 0
        bodydf = b2.b2BodyDef()
        bodydf.position = utils.pixelToWorld(x, y)
        bodydf.type = b2.b2_dynamicBody
        bodydf.userData = self
        self.body:b2.b2Body = world.CreateBody(bodydf)

        boxshape = b2.b2PolygonShape(box=utils.pixelToWorld(w/2, h/2))
        fd = b2.b2FixtureDef()
        fd.shape=boxshape
        fd.density = 1
        fd.restitution = 0
        fd.friction = 1
        self.body.CreateFixture(fd)
        pass

    def draw(self, screen:pygame.Surface):
        position:b2.b2Vec2 = utils.worldToPixel(self.body.position.copy())
        position.y = screen.get_height()-position.y
        current_texture = self.images[self.currentStatus]
    
        if current_texture.get_size() != (self.w, self.h):
            current_texture = pygame.transform.scale(current_texture, (int(self.w), int(self.h)))
            
        screen.blit(current_texture, (position.x - self.w/2, position.y - self.h/2))
        

    def update(self, world):
        '''
        if self.collided:
            if self.currentStatus < 3:
                self.currentStatus = self.currentStatus+1
                self.setLinearVelocity(0, 0)
                self.setAngularVelocity(0)
            
            if self.currentStatus == 3: 
                self.destroy(world)
                
        pass
        '''
        if self.collided:
            seconds = time.time()

        # Iniciem el temporitzador només una vegada
            if self.timer == 0:
                self.prevSec = seconds
                self.timer = 1

            elapsed = seconds - self.prevSec

            if self.currentStatus < 3:
                # Canviem d’estat només un cop per segon (ajusta si vols més ràpid/lent)
                if elapsed > 0.3:
                    self.currentStatus += 1
                    self.collided = False
                    self.prevSec = seconds  # Resetejem el temps per la següent transició
                    self.setLinearVelocity(0, 0)
                    self.setAngularVelocity(0)

            if self.currentStatus == 3:
                self.destroy(world)

    def destroy(self, world:b2.b2World):
        world.DestroyBody(self.body)
        self.isRemoved = True

    def setLinearVelocity(self, x:float, y:float, scale:float=5):
        self.body.linearVelocity = scale*utils.pixelToWorld(x, y)

    def setAngularVelocity(self, a:float):
        self.body.angularVelocity = a

    def boxCollided(self):
        if(not self.collided):
            self.collided = True
            self.prevSec = time.time()
        pass