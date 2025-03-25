import pygame
import Box2D as b2
import utils

class Box:
    def __init__(self, world:b2.b2World, x:float, y:float, w:float, h:float, images:list[pygame.Surface]):
        self.w = w
        self.h = h
        self.images = images

        self.isRemoved = False
        self.currentStatus = 0 #0 is alive, 1 is collided 2 is toDestroy

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
        
        pygame.draw.rect(screen, "lightgray", (position.x-self.w/2, position.y-self.h/2, self.w, self.h))
        pygame.draw.rect(screen, "black", (position.x-self.w/2, position.y-self.h/2, self.w, self.h), 1)
        pass

    def update(self):
        pass

    def destroy(self, world:b2.b2World):
        world.DestroyBody(self.body)
        self.isRemoved = True