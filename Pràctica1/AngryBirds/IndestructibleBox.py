import pygame
import Box2D as b2
import utils

class IndestructibleBox():
    def __init__(self, world, x, y, w, h):
        self.images = pygame.image.load("assets/blocks/indestructible/1.png")
        self.w = w
        self.h = h
        self.isRemoved = False
        self.collided = False
        bodydf = b2.b2BodyDef()
        bodydf.position = utils.pixelToWorld(x, y)
        bodydf.type = b2.b2_staticBody
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
        current_texture = self.images
    
        if current_texture.get_size() != (self.w, self.h):
            current_texture = pygame.transform.scale(current_texture, (int(self.w), int(self.h)))
            
        screen.blit(current_texture, (position.x - self.w/2, position.y - self.h/2))

    def update(self, world):
        pass
    def destroy(self, world:b2.b2World):
        world.DestroyBody(self.body)
        self.isRemoved = True