import pygame
import numpy as np
import Box2D as b2
from Bird import Bird
import utils
import time

#Classe que representa l'ocell gran vermell del joc

class Big(Bird):
    def __init__(self, world:b2.b2World, x:float, y:float, images:list[pygame.Surface]):
        self.radius = 50
        super().__init__(world, x, y, self.radius, images)

        self.body.DestroyFixture(self.body.fixtures[0])

        # Crear un nou fixture amb la densitat modificada
        circleshape = b2.b2CircleShape()
        circleshape.radius = utils.pixelToWorld(self.radius)

        fd = b2.b2FixtureDef()
        fd.shape = circleshape
        fd.density = 15  # Densitat modificada
        fd.restitution = 0.5
        fd.friction = 0.3
        self.body.CreateFixture(fd)