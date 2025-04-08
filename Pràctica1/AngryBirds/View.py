import pygame as py
import utils
from Button import Button

class View:
    def __init__ (self, screen, levelManager):
        self.screen = screen
        self.levelManager = levelManager

        # Start screen UI assets
        self.play_button = Button(py.image.load("assets/ui/buttons/play.png"), 500, 250, 200, 100)
    
        # Menu screen UI assets
        self.level_1_button = Button(py.image.load("assets/ui/buttons/lvl1.png"), 230, 250, 130, 130)
        self.level_2_button = Button(py.image.load("assets/ui/buttons/lvl2.png"), 530, 250, 130, 130)
        self.level_3_button = Button(py.image.load("assets/ui/buttons/lvl3.png"), 830, 250, 130, 130)

    def drawStart(self):
        self.screen.fill('white')
        menu_bg = py.transform.scale(py.image.load("assets/ui/background/main_bg.png"), (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(menu_bg, (0, 0))

        game_title = py.transform.scale(py.image.load("assets/ui/titles/main_title.png"), (400, 150))
        self.screen.blit(game_title, (400, 50))

        self.play_button.draw(self.screen)
        pass

    def drawMenu(self):
        self.screen.fill('white')

        lvl_bg = py.transform.scale(py.image.load("assets/ui/background/main_bg.png"), (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(lvl_bg, (0, 0))

        game_title = py.transform.scale(py.image.load("assets/ui/titles/nivells_title.png"), (200, 75))
        self.screen.blit(game_title, (500, 125))

        self.level_1_button.draw(self.screen)
        self.level_2_button.draw(self.screen)
        self.level_3_button.draw(self.screen)
        pass

    def drawLevel(self, levelManager):
        levelManager.draw()
        pass


