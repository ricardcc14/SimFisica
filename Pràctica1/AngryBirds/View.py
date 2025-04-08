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

        self.back_menu_button = Button(py.image.load("assets/ui/buttons/back.png"), 50, 50, 70, 70)
        self.back_lvl_button = Button(py.image.load("assets/ui/buttons/back.png"), 1100, 30, 70, 70)

        self.end_menu_button = Button(py.image.load("assets/ui/buttons/menu.png"), 420, 370, 100, 100)
        self.end_repeat_button = Button(py.image.load("assets/ui/buttons/repeat.png"), 550, 370, 100, 100)
        self.end_next_button = Button(py.image.load("assets/ui/buttons/next.png"), 680, 360, 120, 120)

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

        self.back_menu_button.draw(self.screen)
        pass

    def drawLevel(self, levelManager):
        levelManager.draw()

        points_title = py.transform.scale(py.image.load("assets/ui/titles/points_title.png"), (110, 30))
        self.screen.blit(points_title, (900, 30))
        self.back_lvl_button.draw(self.screen)

        pass

    def drawEndLevel(self, last_level, stars, points):

        print("ei")

        self.screen.fill('white')
        end_lvl_bg = py.transform.scale(py.image.load("assets/ui/background/main_bg.png"), (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(end_lvl_bg, (0, 0))

        panel_route = "assets/ui/points/level_"+ str(stars) +"_stars.png"
        info_panel = py.transform.scale(py.image.load(panel_route), (500, 350))
        self.screen.blit(info_panel, (350, 50))

        font = py.font.Font("assets/ui/font/angrybirds-regular.ttf", 40)
        text = font.render(str(points), True, 'black')
        text_points = text.get_rect(center=(600, 230))
        self.screen.blit(text, text_points)

        self.end_menu_button.draw(self.screen)
        self.end_repeat_button.draw(self.screen)

        if(last_level != 3):
            self.end_next_button.draw(self.screen)



        pass



