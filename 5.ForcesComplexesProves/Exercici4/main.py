# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
from Ball import Ball
from Liquid import Liquid

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
ball = Ball(40, 200000000, np.array([screen.get_width()/2, 340]), 'brown')
gravity = np.array([0, 9.81])
moveByMouse = False

liquid = Liquid("light blue", 250, 1000)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()            
            if (ball.detect_click(x, y)):
                moveByMouse = True
                ball.set_new_position(y)

        elif event.type == pygame.MOUSEMOTION:
            if (moveByMouse):
                x,y = pygame.mouse.get_pos()            
                ball.set_new_position(y)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if (moveByMouse):
                moveByMouse = False
                x,y = pygame.mouse.get_pos()            
                ball.set_new_position(y)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    
    if (moveByMouse == False):
        #Aplicar gravetat
        ball.apply_gravity_force(gravity)

        #Aplicar força de flotació
        if (liquid.ball_is_inside(ball, screen)):
            ball.apply_flotation_force(liquid, gravity, screen)
           
        ball.checkScreenEdges(screen)        
        ball.update(factor/frames, screen)
        liquid.draw(screen)
        ball.draw(screen)

    else:
        liquid.draw(screen)
        ball.checkScreenEdges(screen)        
        ball.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()