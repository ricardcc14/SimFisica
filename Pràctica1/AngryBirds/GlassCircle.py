import pygame
import Box2D as b2
from Circle import Circle
import utils

class Circle:
    def __init__(self, world:b2.b2World, x:float, y:float, radius:float, images:list[pygame.Surface]):
        super().__init__(world, x, y, radius, images)