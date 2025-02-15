import pygame
import numpy as np

class Ball:
    def __init__ (self, radius, mass, pos_initial):
        self.radius = radius
        self.mass = mass
        self.pos = np.array(pos_initial)
        self.vel = np.array(np.zeros(2))
        self.acc = np.array(np.zeros(2))


    def apply_force(self, dt):
        #self.acc += force / self.mass
     
        self.acc = self.acc + np.array([0, 9.81]) * dt #gravity

    def update(self, dt):
        self.vel = self.vel + self.acc * dt
        self.pos = self.pos + self.vel * dt + 0.5 * (self.acc ** dt)
        self.acc = np.array([0, 0])
        if (self.pos[1] > 600 - self.radius):
            self.vel = 0.99 * self.vel
            self.vel[1] = -self.vel[1]

        if (self.pos[1] > 600 - self.radius):
            self.pos[1] = 600 - self.radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.pos, self.radius)
        
