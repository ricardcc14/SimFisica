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
center_ball = Ball(10, np.power(10, 14), [400, 300], [0, 0], "orange")
center_ball.apply_force([0,0])

ball1 = Ball(20, 10, [150, 200], [1, 0], "light blue")
ball2 = Ball(20, 10, [650, 200], [-1.2, 1], "pink")
ball3 = Ball(20, 10, [450, 100], [0, 1.3], "yellow")
ball4 = Ball(20, 10, [250, 450], [0.5, -0.2], "turquoise")

balls = [center_ball, ball1, ball2, ball3, ball4]


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for ball in balls:
        ball.universal_gravity(balls)
        #ball.checkScreenEdges(screen)
        ball.update(factor/frames)
        ball.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()