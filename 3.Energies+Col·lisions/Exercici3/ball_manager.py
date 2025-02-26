import pygame
import numpy as np
from ball import Ball

class Ball_Manager:

    def __init__ (self, balls):
        self.balls = balls

    def renderAllBalls(self, dt, screen, move):
        if move == True:
            for ball in self.balls:
                ball.checkScreenEdges(screen)
                self.check_collision()
                ball.update(dt)
                ball.apply_normal_and_friction_force(0, 0.001)
                ball.draw(screen)

        else:
            for ball in self.balls:
                ball.checkScreenEdges(screen)
                ball.draw(screen)
            

    def check_collision(self):
        num_balls = len(self.balls)
        for i in range(num_balls):
            for j in range(i + 1, num_balls): 
                ball1 = self.balls[i]
                ball2 = self.balls[j]
                distance = np.linalg.norm(ball1.pos - ball2.pos)
                sum_radi = ball1.radius + ball2.radius
        
                if distance <= sum_radi:
                    ball1.collision_ball(ball2)
                        


