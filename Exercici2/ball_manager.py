import pygame
import numpy as np
from ball import Ball

class Ball_Manager:

    def __init__ (self, radius, mass):
        self.balls = []
        self.balls_radius = radius
        self.balls_mass = mass

    def addBallWithAppliedForce(self, mouse_start_pos, mouse_end_pos):
        #Create new ball object
        ball = Ball(self.balls_radius, self.balls_mass, mouse_end_pos)

        #Calculate applied force 
        force_vector = 1000*(np.array(mouse_end_pos) - np.array(mouse_start_pos))

        #Apply new force
        ball.apply_force(force_vector)

        #Save ball
        self.balls.append(ball)

    def renderAllBalls(self, dt, screen):
        for ball in self.balls:
            ball.checkScreenEdges(screen)
            ball.update(dt)
            ball.draw(screen)


