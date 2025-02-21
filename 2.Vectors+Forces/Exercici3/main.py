import pygame
import numpy as np
from Ball import Ball

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
frames = 60
running = True

# Exercise setup
gravity = np.array([0, -9.8])
coef = 0.5
angle = np.pi / 6
factor = 5

ball = Ball(radius=25, mass=10, position=np.array([100, 429], dtype=np.float64))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        match(event.type):
            case pygame.QUIT:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # RENDER YOUR GAME HERE
    pygame.draw.polygon(screen, 'gray90', [(0, screen.get_height()), (0, screen.get_height()-(np.sqrt(3)/3)*screen.get_width()), (screen.get_width(), screen.get_height())])
    pygame.draw.line(screen, 'black', (0, screen.get_height()-(np.sqrt(3)/3)*screen.get_width()), (screen.get_width(), screen.get_height()))

    ball.apply_gravity_force(gravity)
    ball.apply_normal_and_friction_force(gravity, angle, coef)

    ball.checkEdges(screen)
    ball.update(factor/frames)
    ball.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames)  # limits FPS to 60

pygame.quit()