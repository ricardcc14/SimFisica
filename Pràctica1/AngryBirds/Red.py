import pygame
import numpy as np
import Box2D as b2
from Bird import Bird
import utils
import time

#Classe que representa l'ocell petit del joc
class Red(Bird):
    def __init__(self, world:b2.b2World, x:float, y:float, images:list[pygame.Surface]):
        self.radius = 25
        super().__init__(world, x, y, self.radius, images)
        

        