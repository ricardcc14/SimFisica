from Box import Box
import pygame
import Box2D as b2
import utils

class StoneBox(Box):
    def __init__(self, world, x, y, w, h, images:list[pygame.Surface]):
        self.images = images
        super().__init__(world, x, y, w, h, images)

        self.body.DestroyFixture(self.body.fixtures[0])

        # Crear un nou fixture amb la densitat modificada
        boxShape = b2.b2PolygonShape()

        boxShape = b2.b2PolygonShape(box=utils.pixelToWorld(w/2, h/2))

        fd = b2.b2FixtureDef()
        fd.shape = boxShape
        fd.density = 8  # Densitat modificada
        fd.restitution = 0.5
        fd.friction = 0.3
        self.body.CreateFixture(fd)