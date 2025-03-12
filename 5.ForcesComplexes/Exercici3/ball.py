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
        self.gravity = np.array([0, -9.81])

        #Paràmetres pel moviment angular
        self.radius_rotation = 100
        self.theta = 0.0
        self.angular_vel = 0.0
        self.angular_acc = 0.01

        #Paràmetres orbitació
        self.semi_major_axis = 220
        self.semi_minor_axis = 100
        self.ecc = (np.sqrt(1 - (self.semi_minor_axis**2 / self.semi_major_axis**2)))
        self.focus = np.array([400 + (self.ecc * self.semi_major_axis), 300])

        self.angular_momentum = np.sqrt(10**4 * self.semi_major_axis * (1 - self.ecc**2))

    def apply_force(self, force):     
        self.acc = self.acc + (np.array(force) / self.mass)

    def update(self, dt):
        '''orbit_radius = (self.semi_major_axis * (1 -self.ecc**2) / (1 + self.ecc * np.cos(self.theta)))
        
        self.angular_vel = self.angular_momentum / (orbit_radius**2)
        
    
        self.theta += self.angular_vel * dt
        self.pos = np.array([self.radius_rotation * np.sin(self.theta) + 400 , self.radius_rotation * np.cos(self.theta) + 300])'''
        
        x = self.semi_major_axis * np.cos(self.theta)
        y = self.semi_minor_axis * np.sin(self.theta)

        self.pos = np.array([x + 400 + self.ecc * self.semi_major_axis, y + 300])
        r = np.linalg.norm(self.pos - self.focus)

        self.angular_vel = self.angular_momentum / (r**2)

        # Actualitza l’angle orbital
        self.theta += self.angular_vel * dt


        print("vel: ", self.angular_vel, "radius: ", r)


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
        w = np.array([-u[1], u[0]])

        #Distància de seguretat
        if (np.abs(np.linalg.norm(other_ball.pos - self.pos)) <= (self.radius + other_ball.radius)):
            self.pos = self.pos + 1.1*(-u * ((self.radius + other_ball.radius) - np.linalg.norm(other_ball.pos - self.pos)))

        #Calcular velocitats finals amb nova base
        x_1 = ((self.mass - other_ball.mass) / (self.mass + other_ball.mass)) * self.vel + ((2 * other_ball.mass)/(self.mass + other_ball.mass)) * other_ball.vel
        x_2 =  ((2 * self.mass) / (self.mass + other_ball.mass)) * self.vel + ((other_ball.mass - self.mass) / (self.mass + other_ball.mass)) * other_ball.vel
        
        self.vel = x_1 * u +  self.vel * w
        other_ball.vel = x_2 * u + other_ball.vel * w

    def draw(self, screen):

        #Draw de la pilota
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

        pygame.draw.circle(screen, "red", (int(self.focus[0]), int(self.focus[1])), 5)

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
    
