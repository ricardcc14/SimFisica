import pygame
import numpy as np

class Ball:
    def __init__ (self, radius, mass, pos_initial):
        self.radius = radius
        self.mass = mass
        self.pos = np.array(pos_initial)
        self.vel = np.array(np.zeros(2))
        self.acc = np.array(np.zeros(2))
        self.gravity = np.array([0, 9.81])

    def apply_force(self, force):     
        self.acc = self.acc + (np.array(force) / self.mass)

    def update(self, dt):
        self.acc = self.acc + self.gravity
        self.vel = self.vel + self.acc * dt
        self.pos = self.pos + self.vel * dt + 0.5 * (self.acc * np.power(dt,2))
        self.acc = np.array([0, 0])


    def get_kinetic_energy(self): 
        energy = np.array([0, 0])
        energy = 0.5 * self.mass * np.pow(self.vel,2)
        return energy   

    def get_potential_energy(self, screen:pygame.Surface):
        energy = np.array([0, 0])
        energy = self.mass * self.gravity * (screen.get_height() - self.pos)
        return energy
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.pos, self.radius)

    def checkScreenEdges(self, screen:pygame.Surface):
        #Bottom edge
        if (self.pos[1] > screen.get_height() - self.radius):
            self.vel[1] = -self.vel[1]
            self.pos[1] = screen.get_height() - self.radius

        #Top edge
        if (self.pos[1] < 0 + self.radius):
            self.vel[1] = -self.vel[1]
            self.pos[1] = self.radius

        #Left edge
        if (self.pos[0] < 0 + self.radius):
            self.vel[0] = -self.vel[0]
            self.pos[0] = self.radius

        #Right edge
        if (self.pos[0] > screen.get_width() - self.radius):
            self.vel[0] = -self.vel[0]
            self.pos[0] = screen.get_width() - self.radius
