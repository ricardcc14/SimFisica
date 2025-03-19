import pygame
import numpy as np

class Ball:
    def __init__ (self, radius, mass, pos_initial, vel_initial, color):
        self.radius = radius
        self.mass = mass
        self.pos = np.array(pos_initial)
        self.vel = vel_initial
        self.acc = np.array(np.zeros(2))
        #self.gravity = np.array([0, 9.81])
        self.color = color

    def apply_force(self, force):     
        self.acc = self.acc + (np.array(force) / self.mass)

    def universal_gravity(self, balls):
        G = 6.67 * 10**-11
        total_force = np.array([0, 0])
        for ball in balls:
            if (ball != self):
                direction = ball.pos - self.pos
                distance = np.linalg.norm(direction)
                if (distance > self.radius + ball.radius):
                    force = (G * self.mass * ball.mass)/ (distance ** 2)
                    force_dir = direction / distance
                    total_force = total_force + force * force_dir
        
        self.apply_force(total_force)
               

    def update(self, dt):
        
        #self.acc = self.acc + self.gravity
        self.vel = self.vel + self.acc * dt
        self.pos = self.pos + self.vel * dt # + 0.5 * (self.acc * np.power(dt,2))
        self.acc = np.array([0, 0])

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

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
