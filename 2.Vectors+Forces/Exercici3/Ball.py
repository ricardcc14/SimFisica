import pygame
import numpy as np

class Ball:
    def __init__(self, radius:int, mass:float, position:np.array):
        self.radius = radius
        self.mass = mass
        self.position = position
        self.velocity = np.zeros(2)
        self.acceleration = np.zeros(2)
        pass

    def update(self, dt):
        self.velocity = self.velocity + self.acceleration * dt
        self.position = self.position + self.velocity * dt + 0.5 * (self.acceleration * np.power(dt,2))
        self.acceleration = np.array([0, 0])
        pass

    def draw(self, screen:pygame.Surface):
        flipped_pos = self.position.copy()
        flipped_pos[1] = screen.get_height() - flipped_pos[1]

        pygame.draw.circle(screen, 'white', flipped_pos, self.radius)
        pygame.draw.circle(screen, 'black', flipped_pos, self.radius, 1)
        pass

    def checkEdges(self, screen:pygame.Surface):
        if(self.position[1] < self.radius):
            self.velocity[1] *= -1
            self.position[1] = self.radius

        if(self.position[0] < self.radius or self.position[0] > screen.get_width()-self.radius):
            self.velocity[0] *= -1
        pass


    def apply_force(self, force):     
        self.acceleration = self.acceleration + (np.array(force) / self.mass)

    def apply_gravity_force(self, gravity):
        self.apply_force(self.mass * gravity)
        pass

    def apply_normal_and_friction_force(self, gravity, inclination, coef):
        N = -(gravity[1] * self.mass * np.cos(inclination))
        #Apply normal force
        self.apply_force([N * np.cos(np.pi / 2 - inclination), N * np.sin(np.pi / 2 - inclination)])
        
        #Apply friction force
        self.apply_force([-coef * N * np.sin(np.pi / 2 - inclination), coef * N * np.cos(np.pi / 2 - inclination)])
        pass