# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
from ball import Ball
# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
frames = 60
factor = 10

#Our setup Create a ball
ball = Ball(60, 500, [400, 300])
ball.apply_force([0,0])

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    ball.checkScreenEdges(screen)
    ball.update(factor/frames)
    ball.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()