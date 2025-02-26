import pygame
import numpy as np
from ball import Ball

class Ball_Manager:

    def __init__ (self, balls):
        self.balls = balls
        

    def renderAllBalls(self, dt, screen):
        for ball in self.balls:
            ball.checkScreenEdges(screen)
            ball.update(dt)
            ball.draw(screen)
            self.check_collision()

    def check_collision(self):
        num_balls = len(self.balls)
        for i in range(num_balls):
            for j in range(i + 1, num_balls): 
                ball1 = self.balls[i]
                ball2 = self.balls[j]
                distance = np.linalg.norm(ball1.pos - ball2.pos)
                sum_radi = ball1.radius + ball2.radius
        
                if distance < sum_radi:
                    
                    ball1.collision_ball(ball2)
                  
                    print("Collision")
                        


