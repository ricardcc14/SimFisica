# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
import freetype as ft
from ball import Ball
from food import Food


# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
frames = 60
factor = 15
render = False

#Our setup 
# Create food
food = Food(20, 'red')

# Create ball with applied force
ball = Ball(30, 10, np.array([350, 350]), 'white')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("teal")

    # RENDER YOUR GAME HERE
    ball.check_collision(screen, food)
    ball.checkScreenEdges(screen)
    ball.update(factor/frames, food)
    ball.draw(screen)
    food.draw(screen)
   

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()