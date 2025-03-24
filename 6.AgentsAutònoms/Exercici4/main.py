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
points = np.array([np.array([0, screen.get_height() / 2]), np.array([250, 400]), np.array([550, 200]), np.array([screen.get_width(), 300])])
path = Path(points, 50, "black", "gray")

# Create ball with applied force
ball_1 = Ball(5, 10, np.array([50, 200]), 'white')
ball_2 = Ball(5, 10, np.array([100, 400]), 'white')
ball_3 = Ball(5, 10, np.array([300, 300]), 'white')
ball_4 = Ball(5, 10, np.array([60, 700]), 'white')
ball_5 = Ball(5, 10, np.array([600, 600]), 'white')
ball_6 = Ball(5, 10, np.array([200, 50]), 'white')

balls = [ball_1, ball_2, ball_3, ball_4, ball_5, ball_6]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("teal")

    # RENDER YOUR GAME HERE
    
    path.draw(screen)

    for ball in balls:
        for other_ball in balls:
            if ball != other_ball:
                ball.check_collision(other_ball)

        ball.checkScreenEdges(screen)
        ball.update(factor/frames, path, screen)
        ball.draw(screen)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()