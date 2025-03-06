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
factor = 5
render = False

#Our setup 

# Create ball with applied force
ball = Ball(25, 10, np.array([400, 300]), 'white')


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("teal")

    # RENDER YOUR GAME HERE
    ball.checkScreenEdges(screen)
    ball.update(factor/frames)
    ball.draw(screen)


    


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()