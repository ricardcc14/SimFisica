from Box import Box
import pygame
import Box2D as b2
import utils

class StoneBox(Box):
    def __init__(self, world, x, y, w, h, images:list[pygame.Surface]):
        self.images = images
        super().__init__(world, x, y, w, h, images)

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