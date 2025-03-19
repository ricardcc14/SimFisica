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

# Títol
font = pygame.font.SysFont("Arial", 30)
ui_title = font.render('Agar.io', True, "white")

# Create food
food_1 = Food(10, 'red')
food_2 = Food(10, 'orange')
food_3 = Food(10, 'gray')
food_4 = Food(10, 'pink')
food_5 = Food(10, 'purple')
food_6 = Food(10, 'green')
food_7 = Food(10, 'turquoise')
food_8 = Food(10, 'black')

food = [food_1, food_2, food_3, food_4, food_5, food_6, food_7, food_8]

# Create ball with applied force
ball_1 = Ball(20, 10, np.array([500, 500]), 'white')
ball_2 = Ball(20, 10, np.array([100, 100]), 'yellow')

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("teal")

    # RENDER YOUR GAME HERE
    screen.blit(ui_title, (30, 30))

    #BALL 1 LOGIC
    ball_1.check_collision(screen, food, ball_2)
    ball_1.checkScreenEdges(screen)
    ball_1.update(factor/frames, food)

    #BALL 2 LOGIC
    #BALL 1 LOGIC
    ball_2.check_collision(screen, food, ball_1)
    ball_2.checkScreenEdges(screen)
    ball_2.update(factor/frames, food)

    ball_1.draw(screen)
    ball_2.draw(screen)

    for f in food:
        f.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames) 

pygame.quit()