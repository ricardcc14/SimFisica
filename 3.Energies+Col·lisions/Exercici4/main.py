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
render = False

#Our setup 

# Títol
font = pygame.font.SysFont("Arial", 20)
ui_title = font.render('Press to start!', True, "white")

# Create ball with applied force
ball = Ball(40, 100, np.array([350, 350]), 'white')

# Create static ball
ball2 = Ball(40, 50, np.array([600, 300]), 'blue')
ball3 = Ball(40, 50, np.array([100, 200]), 'red')
ball4 = Ball(40, 50, np.array([600, 500]), 'orange')
ball5 = Ball(40, 50, np.array([250, 400]), 'green')
ball6 = Ball(40, 50, np.array([500, 300]), 'yellow')
ball7 = Ball(40, 50, np.array([100, 400]), 'purple')
ball8 = Ball(40, 50, np.array([400, 450]), 'black')

balls = [ball, ball2, ball3, ball4, ball5, ball6, ball7, ball8]

# Insert 
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            render = True
            ball.apply_force([100000,0])


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("teal")

    # RENDER YOUR GAME HERE
    if (render == False):
        screen.blit(ui_title, (30, 30))

    ball_manager.renderAllBalls(factor/frames, screen, render)


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()