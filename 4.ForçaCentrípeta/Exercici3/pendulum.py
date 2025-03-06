import pygame
import numpy as np

class Pendulum:
    def __init__ (self, radius, mass, pos_initial, color):
        self.radius = radius
        self.mass = mass
        self.color = color
        self.pos = np.array(pos_initial)
        self.vel = np.array(np.zeros(2))
        self.acc = np.array(np.zeros(2))
        self.gravity = 9.81

        #Paràmetres pel moviment angular
        self.radius_rotation = 300
        self.theta = 0 * np.pi / 180.0
        self.angular_vel = 0.0

        self.angular_acc = 0.0
        self.acc_tang = 0.0
        self.acc_cent = 0.0

    def apply_force(self, force):     
        self.acc = self.acc + (np.array(force) / self.mass)

    def apply_ballistic(self, bullet_mass, bullet_vel):
        self.vel = (bullet_mass * bullet_vel) / (self.mass + bullet_mass)
        self.angular_vel = self.vel / self.radius_rotation

    def update(self, dt, screen):

        self.acc_tang = -self.gravity * np.sin(self.theta)
        self.angular_acc = self.acc_tang / self.radius_rotation

        self.angular_vel += self.angular_acc * dt

        self.theta += self.angular_vel * dt


        self.pos = np.array([
            screen.get_width()/2 + self.radius_rotation * np.sin(self.theta),  # X
            screen.get_height()/4  + self.radius_rotation * np.cos(self.theta)   # Y
        ])
    

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
        # Draw de la corda
        pygame.draw.line(screen, "black", (screen.get_width()/2, screen.get_width()/4), self.pos, 2)

        # Draw de la pilota
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
    
