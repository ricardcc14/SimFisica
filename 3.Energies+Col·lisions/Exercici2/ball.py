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
        
        final_vel = np.array([0, 0])
        final_vel = ((self.mass - other_ball.mass) / (self.mass * other_ball.mass)) * self.vel + ((2 * other_ball.mass) / (self.mass + other_ball.mass)) * other_ball.vel

        direction = self.pos - other_ball.pos
        norm_direction = np.linalg.norm(direction)
        perpendicular = np.array([-direction[1], direction[0]])
        norm_perpendicular = np.linalg.norm(perpendicular)

        angle1 = np.arccos(np.dot(self.vel, direction) / (np.linalg.norm(self.vel) * np.linalg.norm(direction)))
        angle2 = np.arccos(np.dot(other_ball.vel, -direction) / (np.linalg.norm(other_ball.vel) * np.linalg.norm(-direction)))


        self.vel = np.linalg.norm(final_vel) * norm_direction * angle1 + np.linalg.norm(final_vel) * norm_perpendicular * angle2
        
        '''direction = self.pos - other_ball.pos
        norm_direction = np.linalg.norm(direction)
        if norm_direction == 0:
            return 
        direction_normalized = direction / norm_direction

        perpendicular = np.array([-direction[1], direction[0]])
        norm_perpendicular = np.linalg.norm(perpendicular)
        if norm_perpendicular == 0:
            return 

        # Normalize the perpendicular vector
        perpendicular_normalized = perpendicular / norm_perpendicular

        # Calculate the final velocity using the correct formula for elastic collisions
        final_vel_self = (
            ((self.mass - other_ball.mass) / (self.mass + other_ball.mass)) * self.vel
            + ((2 * other_ball.mass) / (self.mass + other_ball.mass)) * other_ball.vel
        )

        final_vel_other = (
            ((other_ball.mass - self.mass) / (self.mass + other_ball.mass)) * other_ball.vel
            + ((2 * self.mass) / (self.mass + other_ball.mass)) * self.vel
        )

        # Decompose the final velocities into components along the collision normal and perpendicular
        self.vel = (
            np.dot(final_vel_self, direction_normalized) * direction_normalized
            + np.dot(self.vel, perpendicular_normalized) * perpendicular_normalized
        )

        other_ball.vel = (
            np.dot(final_vel_other, -direction_normalized) * -direction_normalized
            + np.dot(other_ball.vel, perpendicular_normalized) * perpendicular_normalized
        )'''
        

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
