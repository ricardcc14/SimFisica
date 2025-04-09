from Box import Box
import pygame
import Box2D as b2
import utils

class GlassBox(Box):
    def __init__(self, world, x, y, w, h, images:list[pygame.Surface]):
        self.images = images
        super().__init__(world, x, y, w, h, images)

        self.body.DestroyFixture(self.body.fixtures[0])

        # Crear un nou fixture amb la densitat modificada
        boxShape = b2.b2PolygonShape()

        boxShape = b2.b2PolygonShape(box=utils.pixelToWorld(w/2, h/2))

        fd = b2.b2FixtureDef()
        fd.shape = boxShape
        fd.density = 1  # Densitat modificada
        fd.restitution = 0.2
        fd.friction = 0.01
        self.body.CreateFixture(fd)

