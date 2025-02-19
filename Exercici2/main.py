# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
from ball import Ball
from ball_manager import Ball_Manager

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
frames = 60

#Our setup: Create a ball manager
ball_manager = Ball_Manager(10, 50)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_end_pos = event.pos
            ball_manager.addBallWithAppliedForce(mouse_start_pos, mouse_end_pos)



    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    dt = clock.tick(frames) / 1000

    # RENDER YOUR GAME HERE
    ball_manager.renderAllBalls(dt, screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 
