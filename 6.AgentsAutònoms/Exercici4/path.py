import pygame
import numpy as np

class Path:
    def __init__ (self, points, width, base_color, line_color):
        self.points = points
        self.width = width
        self.base_color = base_color
        self.line_color = line_color

    def draw(self, screen):
        for i in range(len(self.points) - 1):
            pygame.draw.line(screen, self.base_color, self.points[i], self.points[i + 1], self.width)
            pygame.draw.line(screen, self.line_color, self.points[i], self.points[i + 1], 2)
        #pygame.draw.lines(screen, self.base_color, False, self.points, self.width)
        #pygame.draw.lines(screen, self.line_color, False, self.points, 2)

    def getVector(self, sense):
        if (len(self.points) == 2):
            if (sense > 0):
                vector = self.points[1] - self.points[0]
            else:
                vector = self.points[0] - self.points[1]

        return (vector / np.linalg.norm(vector))
                        
    def getPathLimits(self, line_origin, line_end):
        #max_height = self.points[0][1] + 25
        #min_height = self.points[0][1] - 25
        #return np.array([max_height, min_height])
        line_vector = line_end - line_origin
        line_vector = line_vector / np.linalg.norm(line_vector)  # Normalitzar

        # Vector perpendicular a la línia (normal)
        normal_vector = np.array([-line_vector[1], line_vector[0]])

        # Aplicar el marge en la direcció perpendicular
        upper_limit = line_origin + normal_vector * 25
        lower_limit = line_origin - normal_vector * 25

        return np.array([upper_limit, lower_limit])
    
    def getOrigin(self, sense):
        if (sense > 0):
            origin = self.points[0]
        else:
            origin = self.points[1]
        return origin
