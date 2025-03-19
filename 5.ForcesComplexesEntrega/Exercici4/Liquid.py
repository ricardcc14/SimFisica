import pygame
import numpy as np
from Ball import Ball

class Liquid:
    def __init__ (self, color, height, density):
        self.color = color
        self.height = height
        self.density = density

    def draw(self, screen):
        # Draw del líquid
        pygame.draw.rect(screen, self.color, [0, screen.get_height() - self.height, screen.get_width(), self.height])

    def ball_is_inside(self, ball, screen):
        if ((screen.get_height() - (ball.pos[1] + ball.radius)) <= (self.height)):
            return True
        else:
            return False
        
