# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
import freetype as ft
from ball import Ball
from ball_manager import Ball_Manager

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
frames = 60
factor = 5

#Our setup Create a ball

ball = Ball(40, 100, [350, 300], 'white')
ball.apply_force([100000,0])

ball2 = Ball(40, 50, [600, 300], 'blue')

balls = [ball, ball2]

ball_manager = Ball_Manager(balls)



def display_energy_bars(ball, screen):
    kinetic = ball.get_kinetic_energy()
    potential = ball.get_potential_energy(screen)
    mechanic = kinetic + potential
    print(str(mechanic))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    ball_manager.renderAllBalls(factor/frames, screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()