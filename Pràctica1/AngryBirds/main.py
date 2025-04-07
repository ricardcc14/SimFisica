
#Libraries
import pygame
import Box2D as b2
import utils

#Managers
from LevelManager import LevelManager
from View import View

from ContactListener import ContactListener
from Surface import Surface
from Bird import Bird
from Box import Box
from Pig import Pig

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
frames = 120
running = True
scene = "start" #start, menu, lvl_1, lvl_2, lvl_3


# Managers initialization
levelManager = LevelManager(screen)

view = View(screen, levelManager)
origin = b2.b2Vec2(0,0)

while running:
    screen.fill('gray')

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start screen events
        elif event.type == pygame.MOUSEBUTTONDOWN and scene == "start":
            if view.play_button.collidepoint(pygame.mouse.get_pos()):
                scene = "menu"

        # Menu screen events
        elif event.type == pygame.MOUSEBUTTONDOWN and scene == "menu":
            if view.level_1_button.collidepoint(pygame.mouse.get_pos()):
                scene = "lvl_1"
                levelNum = 1
                levelManager.loadLevel(levelNum)
            elif view.level_2_button.collidepoint(pygame.mouse.get_pos()):
                scene = "lvl_2"
                levelNum = 2
                levelManager.loadLevel(levelNum)
            elif view.level_3_button.collidepoint(pygame.mouse.get_pos()):
                scene = "lvl_3"
                levelNum = 3
                levelManager.loadLevel(levelNum)

        # Level screen events
        
        elif event.type == pygame.MOUSEBUTTONDOWN and (scene == "lvl_1" or scene == "lvl_2" or scene == "lvl_3"):
            mouse_pos = b2.b2Vec2(event.pos[0], event.pos[1])
            levelManager.handleMouseDown(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONUP and (scene == "lvl_1" or scene == "lvl_2" or scene == "lvl_3"):
            mouse_pos = b2.b2Vec2(event.pos[0], event.pos[1])
            levelManager.handleMouseUp(mouse_pos)
        

    if scene == "start":
        view.drawStart()
    elif scene == "menu":
        view.drawMenu()
    elif scene == "lvl_1" or scene == "lvl_2" or scene == "lvl_3":
        levelManager.runLevel()
        view.drawLevel(levelManager)

    pygame.display.flip()
    clock.tick(frames)

    


pygame.quit()


'''
# Box2D
world = b2.b2World()
time_step = 1/frames
vel_iters, pos_iters = 8, 3
contactListener = ContactListener()
world.contactListener = contactListener

# Images
bkgSky = pygame.image.load("assets/sky.png")
bkgFloor = pygame.image.load("assets/floor.png")

basicBird = []
basicBird.append(pygame.image.load("assets/BasicBird.png"))
basicBird.append(pygame.image.load("assets/BasicBirdCollided.png"))
basicBird.append(pygame.image.load("assets/BasicBirdDisappear.png"))

# Data
mouse_pressed = False
origin = b2.b2Vec2(0, 0)

surface = Surface(world, screen.get_width()/2, 100, screen.get_width()*2, 5)
birds:list[Bird] = []
boxes:list[Box] = []
pigs:list[Pig] = []

# birds.append(Bird(world, 300, 300, 25, basicBird))

boxes.append(Box(world, 1000, 200, 100, 100, None))
boxes.append(Box(world, 1000, 300, 100, 100, None))

pigs.append(Pig(world, 1000, 400, 50, None))
                 
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            origin = b2.b2Vec2(pygame.mouse.get_pos())
            mouse_pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            end = b2.b2Vec2(pygame.mouse.get_pos())
            direction = origin - end
            birds.append(Bird(world, origin.x, screen.get_height()-origin.y, 25, basicBird))
            birds[-1].setLinearVelocity(direction.x, -direction.y)
            mouse_pressed = False
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # RENDER YOUR GAME HERE
    world.Step(time_step, vel_iters, pos_iters)

    utils.drawRotatedImage(screen, bkgSky, b2.b2Vec2(screen.get_width()/2, screen.get_height()/2), screen.get_width(), screen.get_height(), 0)
    utils.drawRotatedImage(screen, bkgFloor, b2.b2Vec2(screen.get_width()/2, screen.get_height()/2+45), screen.get_width(), screen.get_height(), 0)

    if(mouse_pressed): pygame.draw.line(screen, "crimson", origin, pygame.mouse.get_pos())

    for i, bird in enumerate(birds):
        if(bird.isRemoved):
            birds.pop(i)
        else:
            bird.update(world)
            bird.draw(screen)

    for i, box in enumerate(boxes):
        if(box.isRemoved):
            boxes.pop(i)
        else:
            box.update()
            box.draw(screen)
    
    for i, pig in enumerate(pigs):
        if(pig.isRemoved):
            pigs.pop(i)
        else:
            pig.update(world)
            pig.draw(screen)

    surface.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(frames)  # limits FPS to 60

pygame.quit()
'''