from Box import Box
import pygame
import Box2D as b2
import utils

class GlassBox(Box):
    def __init__(self, world, x, y, w, h, images:list[pygame.Surface]):
        self.images = images
        super().__init__(world, x, y, w, h, images)

