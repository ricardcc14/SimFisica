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
        print("U: "+str(u))
        w = np.array([-u[1], u[0]])
        print("W: "+str(w))

        #Calcular angles per les projeccions
        print("Vel 1: "+str(self.vel))
        print("Vel 2: "+str(other_ball.vel))

        if np.linalg.norm(self.vel) > 0:
            theta = np.arccos(np.dot(self.vel, u) / (np.linalg.norm(self.vel) * np.linalg.norm(u)))
        else:
            theta = 0

        print("Theta: "+str(theta))

        if np.linalg.norm(other_ball.vel) > 0:
            phi = np.arccos(np.dot(other_ball.vel, -u) / (np.linalg.norm(other_ball.vel) * np.linalg.norm(u)))
        else:
            phi = 0

        print("Phi: "+str(phi))

        #Calcular canvi de base
        vel_i_1 = np.linalg.norm(self.vel) * np.cos(theta) * u + np.linalg.norm(self.vel) * np.sin(theta) * w
        vel_i_2 = np.linalg.norm(other_ball.vel) * np.cos(phi) * u + np.linalg.norm(other_ball.vel) * np.sin(phi) * w

        vel_i_1_u = np.linalg.norm(self.vel) * np.cos(theta)
        vel_i_1_w = np.linalg.norm(self.vel) * np.sin(theta)

        vel_i_2_u = -np.linalg.norm(other_ball.vel) * np.cos(phi)
        vel_i_2_w = -np.linalg.norm(other_ball.vel) * np.sin(phi)
        
 
        print("Vel_i_1_u: "+str(vel_i_1_u))
        print("Vel_i_1_w: "+str(vel_i_1_w))
        print("Vel_i_2_u: "+str(vel_i_2_u))
        print("Vel_i_2_2: "+str(vel_i_2_w))

        #Calcular velocitats finals amb nova base
        x_1 = ((self.mass - other_ball.mass) / (self.mass + other_ball.mass)) * vel_i_1_u + ((2 * other_ball.mass)/(self.mass + other_ball.mass)) * vel_i_2_u
        x_2 =  ((2 * self.mass) / (self.mass + other_ball.mass)) * vel_i_1_u + ((other_ball.mass - self.mass) / (self.mass + other_ball.mass)) * vel_i_2_u
        
        print("X_1: "+str(x_1))
        print("X_2: "+str(x_2))
        

        self.vel = x_1 * u +  vel_i_1_w * w
        other_ball.vel = x_2 * u + vel_i_2_w * w

        print("VEL FINAL 1: "+str(self.vel))
        print("VEL FINAL 2: "+str(other_ball.vel))



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
