#Libraries
import pygame
import Box2D as b2
import utils

#Managers
from LevelManager import LevelManager
from View import View

from ContactListener import ContactListener
from PointsManager import PointsManager
from Surface import Surface
from Bird import Bird
from Box import Box
from Pig import Pig
from Button import Button


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
frames = 120
running = True
scene = "start" #start, menu, lvl_1, lvl_2, lvl_3, lvl_end
currentlevel = 0

# Managers initialization
pointsManager = PointsManager(3)
levelManager = LevelManager(screen, pointsManager)

view = View(screen, levelManager)
origin = b2.b2Vec2(0,0)

pygame.mixer.init()
sound = pygame.mixer.Sound("assets/ui/music/AngryBirdsMusic.mp3")
sound.set_volume(0.3)  
sound.play()

while running:
    screen.fill('gray')
    pygame.display.set_caption('Angry Birds')
    currentlevel_index = currentlevel - 1

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start screen events
        elif event.type == pygame.MOUSEBUTTONDOWN and scene == "start":
            if view.play_button.isClicked(pygame.mouse.get_pos()):
                scene = "menu"

        # Menu screen events
        elif event.type == pygame.MOUSEBUTTONDOWN and scene == "menu":
            if view.level_1_button.isClicked(pygame.mouse.get_pos()):
                scene = "lvl_1"
                currentlevel = 1

                levelManager.loadLevel(currentlevel)

            elif view.level_2_button.isClicked(pygame.mouse.get_pos()):
                scene = "lvl_2"
                currentlevel= 2

                levelManager.loadLevel(currentlevel)

            elif view.level_3_button.isClicked(pygame.mouse.get_pos()):
                scene = "lvl_3"

                currentlevel = 3
                levelManager.loadLevel(currentlevel)

            elif view.back_menu_button.isClicked(pygame.mouse.get_pos()):

                scene = "start"
            
        # Level screen events
        elif event.type == pygame.MOUSEBUTTONDOWN and (scene == "lvl_1" or scene == "lvl_2" or scene == "lvl_3") and (view.back_lvl_button.isClicked(pygame.mouse.get_pos()) == False):
            mouse_pos = b2.b2Vec2(event.pos[0], event.pos[1])
            levelManager.handleMouseDown(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONUP and (scene == "lvl_1" or scene == "lvl_2" or scene == "lvl_3") and (view.back_lvl_button.isClicked(pygame.mouse.get_pos()) == False):
            mouse_pos = b2.b2Vec2(event.pos[0], event.pos[1])
            levelManager.handleMouseUp(mouse_pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and view.back_lvl_button.isClicked(pygame.mouse.get_pos()) and (scene == "lvl_1" or scene == "lvl_2" or scene == "lvl_3"):
            scene = "menu"
            levelManager.destroyAllObjects()

        # End level screen events
        elif view.end_menu_button.isClicked(pygame.mouse.get_pos()) and scene == "lvl_end" and event.type == pygame.MOUSEBUTTONDOWN:
            scene = "menu"
        elif view.end_repeat_button.isClicked(pygame.mouse.get_pos()) and scene == "lvl_end" and event.type == pygame.MOUSEBUTTONDOWN:
            scene = "lvl_"+str(currentlevel)
            levelManager.loadLevel(currentlevel)
        elif view.end_next_button.isClicked(pygame.mouse.get_pos()) and scene == "lvl_end" and event.type == pygame.MOUSEBUTTONDOWN:
            currentlevel = currentlevel + 1
            scene = "lvl"+str(currentlevel)
            levelManager.loadLevel(currentlevel)

    if scene == "start":
        view.drawStart()
    elif scene == "menu":
        view.drawMenu()
    elif scene == "lvl_1" or scene == "lvl_2" or scene == "lvl_3":
        levelManager.runLevel()
        if(pointsManager.checkIfLevelIsPassed(currentlevel_index)):
            scene = "lvl_end"
            levelManager.destroyAllObjects()
            view.drawEndLevel(currentlevel, pointsManager.getStars(currentlevel_index), pointsManager.getPoints(currentlevel_index))
        else:
            view.drawLevel(levelManager, pointsManager.getPoints(currentlevel_index))
    elif scene == "lvl_end":
        view.drawEndLevel(currentlevel, pointsManager.getStars(currentlevel_index), pointsManager.getPoints(currentlevel_index))

    pygame.display.flip()
    clock.tick(frames)

pygame.quit()