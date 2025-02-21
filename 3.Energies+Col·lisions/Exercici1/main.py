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
ball = Ball(40, 100, [400, 300])
ball.apply_force([0,0])

def display_energy_bars(ball, screen):
    kinetic = ball.get_kinetic_energy()
    potential = ball.get_potential_energy(screen)
    mechanic = kinetic + potential
    print(str(mechanic))

    pygame.draw.rect(screen, "orange", pygame.Rect(30, 30, kinetic[1] / (screen.get_width()), 30), border_radius=5)
    pygame.draw.rect(screen, "yellow", pygame.Rect(30, 65, potential[1] / (screen.get_width()), 30), border_radius=5)
    pygame.draw.rect(screen, "red", pygame.Rect(30, 100, mechanic[1] / (screen.get_width()), 30), border_radius=5)



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

    display_energy_bars(ball, screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()