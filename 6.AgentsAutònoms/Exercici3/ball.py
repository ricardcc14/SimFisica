import pygame
import numpy as np
from path import Path

class Ball:
    def __init__ (self, radius, mass, pos_initial, color):
        self.radius = radius
        self.mass = mass
        self.color = color
        self.pos = np.array(pos_initial)
        self.vel = np.array([1,0])
        self.acc = np.array(np.zeros(2))
        self.gravity = np.array([0, 9.81])
        self.max_speed = 10
        self.max_steering = 1

        self.future_pos = np.array([0,0])
        self.project_pos = np.array([0,0])
        self.target_pos = np.array([0,0])
        

    def apply_force(self, force):     
        self.acc = self.acc + (np.array(force) / self.mass)
   
    def update(self, screen, dt, path):
        line_vector = path.getVector(self.vel[0])
        line_origin = path.getOrigin(self.vel[0])
        limits = path.getPathLimits()

        self.future_pos = self.pos + 5 * self.vel

        normal_vector = np.array([-line_vector[1], line_vector[0]])
        print("Normal vector", str(normal_vector))
        projection_vector = np.dot(self.future_pos - line_origin, line_vector) * line_vector
        self.project_pos = line_origin + projection_vector
        print("Projection vector: ", str(normal_vector))

        #self.project_pos = np.array([0,0])
        #self.project_pos[0] = self.future_pos[0]
        #self.project_pos[1] = 300
        #self.project_pos = self.future_pos + projection_vector

        self.target_pos = self.project_pos + 20*line_vector
       
        #Trobar direcció desitjada
        desired_direction = self.target_pos - self.pos
        desired_direction_norm = np.linalg.norm(desired_direction)

        #Limitar direcció màxima
        if (desired_direction_norm > self.max_speed):
            desired_direction = (desired_direction / desired_direction_norm) * self.max_speed

        if (self.pos[1] >= limits[0] or self.pos[1] <= limits[1]):
            #Calcular força de rotació
            steering_force_dir = desired_direction - self.vel
            self.apply_force(steering_force_dir * self.max_steering)

        self.vel = self.vel + self.acc * dt

        vel_norm = np.linalg.norm(self.vel)
        if vel_norm > self.max_speed:
         self.vel = (self.vel / vel_norm) * self.max_steering

        self.pos = self.pos + self.vel * dt 
        self.acc = np.array([0, 0])

        print("Position: " , self.pos)
        print("Target: " , self.target_pos)
        print("Projection: ", self.project_pos)
        print("Limits: " , str(limits))

        self.checkScreenEdges(screen)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.pos, self.radius)
        pygame.draw.circle(screen, "blue", self.future_pos, self.radius/2)
        pygame.draw.circle(screen, "red", self.project_pos, self.radius/2)
        pygame.draw.circle(screen, "green", self.target_pos, self.radius/2)


    def check_collision(self, screen, food, other_ball):
        #CHECK FOR FOOD COLISION
        for f in food:
            distance2food = np.linalg.norm(self.pos - f.pos)
            sum_radi = self.radius + f.radius

            if distance2food <= sum_radi:
                f.reposition(screen)
                if self.radius < 100:
                    self.radius += 0.25*f.radius


        #CHECK FOR OTHER BALL COLISION
        distance2ball = np.linalg.norm(self.pos - other_ball.pos)
        sum_radi = self.radius + other_ball.radius

        if distance2ball <= sum_radi:
            self.collision_ball(other_ball)
            if (self.radius > other_ball.radius):
                if self.radius < 100:
                    self.radius += 0.25*other_ball.radius
                other_ball.pos = np.array([np.random.randint(self.radius, 800 - self.radius), np.random.randint(self.radius, 600 - self.radius)])
                other_ball.radius = 10


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
            self.pos = self.pos + 1.2*(-u * ((self.radius + other_ball.radius) - np.linalg.norm(other_ball.pos - self.pos)))

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
    
