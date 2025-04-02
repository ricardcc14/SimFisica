import pygame
import Box2D as b2
import utils

class Circle:
    def __init__(self, world:b2.b2World, x:float, y:float, radius:float, images:list[pygame.Surface], material):
        self.radius = radius
        self.images = images

        self.material = material

        self.isRemoved = False
        self.currentStatus = 0 #0 is alive, 1 is collided 2 is toDestroy

        bodydf = b2.b2BodyDef()
        bodydf.position = utils.pixelToWorld(x, y)
        bodydf.type = b2.b2_dynamicBody
        bodydf.userData = self
        self.body:b2.b2Body = world.CreateBody(bodydf)

        circleshape = b2.b2CircleShape(radius=utils.pixelToWorld(radius))
        fd = b2.b2FixtureDef()
        fd.shape=circleshape
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