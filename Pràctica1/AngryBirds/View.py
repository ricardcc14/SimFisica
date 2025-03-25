import pygame as py
import utils

class View:
    def __init__ (self, screen, levelManager):
        self.screen = screen
        self.levelManager = levelManager
        # Start screen assets
        self.play_button = py.Rect(500, 250, 200, 80)


        # Menu screen assets
        self.level_1_button = py.Rect(100, 250, 200, 80)
        self.level_2_button = py.Rect(500, 250, 200, 80)
        self.level_3_button = py.Rect(900, 250, 200, 80)

        # Level screen assets



    def drawStart(self):
        self.screen.fill('white')

        
        py.draw.rect(self.screen, 'blue', self.play_button)

        font = py.font.Font(None, 40)
        text = font.render("PLAY", True, 'white')
        text_rect = text.get_rect(center=(600, 400))

        self.screen.blit(text, text_rect)
        
        pass

    def drawMenu(self):
        self.screen.fill('blue')
        
        py.draw.rect(self.screen, 'green', self.level_1_button)
        py.draw.rect(self.screen, 'green', self.level_2_button)
        py.draw.rect(self.screen, 'green', self.level_3_button)
        pass

    def drawLevel(self, levelManager):
        
        levelManager.draw(self.screen)
        pass