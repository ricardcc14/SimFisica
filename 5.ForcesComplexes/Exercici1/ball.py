import pygame
import numpy as np

class Ball:
    def __init__ (self, radius, mass, pos_initial):
        self.radius = radius
        self.mass = mass
        self.pos = np.array(pos_initial)
        self.vel = np.array(np.zeros(2))
        self.acc = np.array(np.zeros(2))
        self.gravity = np.array([0, -9.81])

    def apply_force(self, force):     
        self.acc = self.acc + (np.array(force) / self.mass)

    def ApplyHooke(self, k, mouse_end_pos):
        force = -k * (self.pos - np.array(mouse_end_pos))
        self.apply_force(force)

    def update(self, dt):
        self.acc = self.acc + self.gravity
        self.vel = self.vel + self.acc * dt
        self.pos = self.pos + self.vel * dt # + 0.5 * (self.acc * np.power(dt,2))
        self.acc = np.array([0, 0])

    def draw(self, screen):
        pos_screen = np.array([self.pos[0], 400 - self.pos[1]])

        pygame.draw.line(screen, "black", [400, 0], pos_screen, 2)

        pygame.draw.circle(screen, "white", pos_screen, self.radius)

    def checkScreenEdges(self, screen:pygame.Surface):
        #Bottom edge
        if (self.pos[1] > screen.get_height() - self.radius):
            self.vel[1] = -self.vel[1]
            self.pos[1] = screen.get_height() - self.radius

        #Top edge
        if (self.pos[1] < 0 + self.radius):
            self.vel = 0.99 * self.vel
            self.vel[1] = -self.vel[1]
            self.pos[1] = self.radius

        #Left edge
        if (self.pos[0] < 0 + self.radius):
            self.vel = 0.99 * self.vel
            self.vel[0] = -self.vel[0]
            self.pos[0] = self.radius

        #Right edge
        if (self.pos[0] > screen.get_width() - self.radius):
            self.vel = 0.99 * self.vel
            self.vel[0] = -self.vel[0]
            self.pos[0] = screen.get_width() - self.radius

    def mouseClickOn(self, mouse_pos):
        distance = np.linalg.norm([self.pos[0], 400- self.pos[1]] - np.array(mouse_pos))
        return distance < self.radius
    
    def stopMotion(self):
        self.vel = np.array([0,0])
        self.acc = np.array([0,0])
