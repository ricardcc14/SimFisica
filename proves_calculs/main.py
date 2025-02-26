# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
import freetype as ft
from ball import Ball

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
frames = 60
factor = 5

#Our setup Create a ball

ball = Ball(20, 5, [400, 401], 'white')
ball.vel = np.array([2, 0])

ball2 = Ball(20, 3, [401, 400], 'blue')
ball2.vel = np.array([-1, 0])


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    ball.vel = np.array([2, 0])
    ball2.vel = np.array([-1, 0])
    ball.collision_ball(ball2)

    ball.draw(screen)
    ball2.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()