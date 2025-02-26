import pygame
import numpy as np

class Ball:
    def __init__ (self, radius, mass, pos_initial, color):
        self.radius = radius
        self.mass = mass
        self.color = color
        self.pos = np.array(pos_initial)
        self.vel = np.array(np.zeros(2))
        self.acc = np.array(np.zeros(2))
        self.gravity = np.array([0, 9.81])

    def apply_force(self, force):     
        self.acc = self.acc + (np.array(force) / self.mass)

    def update(self, dt):
        #self.acc = self.acc + self.gravity
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
        
    def collision_ball(self, other_ball):

        #Trobar els vectors unitaris de l'eix de xoc
        u = np.array(other_ball.pos - self.pos) / np.linalg.norm(other_ball.pos - self.pos)

        #Distància de seguretat
        if (np.abs(np.linalg.norm(other_ball.pos - self.pos)) <= (self.radius + other_ball.radius)):
            self.pos = self.pos + 1.1*(-u * ((self.radius + other_ball.radius) - np.linalg.norm(other_ball.pos - self.pos)))

        #Trobar els vectors unitaris de l'eix de xoc
        w = np.array([-u[1], u[0]])

        #Calcular angles per les projeccions
        if np.linalg.norm(self.vel) > 0 and np.linalg.norm(other_ball.pos) > 0:
            theta = np.arccos(np.dot(u, self.vel) / (np.linalg.norm(self.vel) * np.linalg.norm(u)))
            if (np.cross(u, self.vel) < 0):
                theta = -theta
        else:
            theta = 0

        if (np.linalg.norm(other_ball.vel) > 0) and np.linalg.norm(other_ball.pos) > 0:
            phi = np.arccos(np.dot(u, other_ball.vel) / (np.linalg.norm(other_ball.vel) * np.linalg.norm(u)))
            if (np.cross(u, other_ball.vel) < 0):
                phi = -phi
        else:
            phi = 0

        #Calcular canvi de base
        vel_i_1 = np.linalg.norm(self.vel) * np.cos(theta) * u + np.linalg.norm(self.vel) * np.sin(theta) * w
        vel_i_2 = np.linalg.norm(other_ball.vel) * np.cos(phi) * u + np.linalg.norm(other_ball.vel) * np.sin(phi) * w

        vel_i_1_u = np.linalg.norm(self.vel) * np.cos(theta)
        vel_i_1_w = np.linalg.norm(self.vel) * np.sin(theta)

        vel_i_2_u = np.linalg.norm(other_ball.vel) * np.cos(phi)
        vel_i_2_w = np.linalg.norm(other_ball.vel) * np.sin(phi)

        #Calcular velocitats finals amb nova base
        x_1 = ((self.mass - other_ball.mass) / (self.mass + other_ball.mass)) * vel_i_1_u + ((2 * other_ball.mass)/(self.mass + other_ball.mass)) * vel_i_2_u
        x_2 =  ((2 * self.mass) / (self.mass + other_ball.mass)) * vel_i_1_u + ((other_ball.mass - self.mass) / (self.mass + other_ball.mass)) * vel_i_2_u
        
        self.vel = x_1 * u +  vel_i_1_w * w
        other_ball.vel = x_2 * u + vel_i_2_w * w

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

    def apply_normal_and_friction_force(self, inclination, coef):
        N = -(self.gravity[1] * self.mass * np.cos(inclination))
        self.apply_force([-coef * N * -self.vel[0], -coef * N * -self.vel[1]])
        pass
    
