# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
import freetype as ft
from ball import Ball
from path import Path

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
frames = 60
factor = 15
render = False

#Our setup 

# Títol
# Create path
points = np.array([np.array([0, screen.get_height() / 2]), np.array([screen.get_width(), screen.get_height() / 2])])
path = Path(points, 50, "black", "gray")

# Create ball with applied force
ball_1 = Ball(5, 10, np.array([50, 200]), 'white')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("teal")

    # RENDER YOUR GAME HERE
    #BALL 1 LOGIC
    ball_1.checkScreenEdges(screen)

    ball_1.update(screen, factor/frames, path)

    path.draw(screen)

    ball_1.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()