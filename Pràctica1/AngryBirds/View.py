import pygame as py
import utils
from Button import Button

class View:
    def __init__ (self, screen, levelManager):
        self.screen = screen
        self.levelManager = levelManager

        # Start screen UI assets
        self.play_button = Button(py.image.load("assets/ui/buttons/play.png"), 500, 250, 200, 80)
        
    
        # Menu screen UI assets
        self.level_1_button = Button(py.image.load("assets/ui/buttons/lvl1.png"), 500, 250, 200, 80)
        self.level_2_button = Button(py.image.load("assets/ui/buttons/lvl2.png"), 500, 250, 200, 80)
        self.level_3_button = Button(py.image.load("assets/ui/buttons/lvl3.png"), 500, 250, 200, 80)

        # Level screen UI assets



    def drawStart(self):
        self.screen.fill('white')

        self.play_button.draw(self.screen)
        pass

    def drawMenu(self):
        self.screen.fill('blue')
        
        self.level_1_button.draw(self.screen)
        self.level_2_button.draw(self.screen)
        self.level_3_button.draw(self.screen)

        pass

    def drawLevel(self, levelManager):
        
        levelManager.draw()
        pass