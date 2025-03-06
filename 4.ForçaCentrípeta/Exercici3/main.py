# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
from pendulum import Pendulum

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
frames = 60
factor = 5
render = False

#Our setup 

# Títol
font = pygame.font.SysFont("Arial", 20)
ui_title = font.render('Press to start!', True, "white")

# Create ball with applied force
pendulum = Pendulum(40, 10, np.array([0, 0]), 'white')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            render = True
            pendulum.apply_ballistic(10, 100)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("teal")

    # RENDER YOUR GAME HERE
    if (render == False):
        screen.blit(ui_title, (30, 30))
    
    pendulum.checkScreenEdges(screen)
    pendulum.update(factor/frames, screen)
    pendulum.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()