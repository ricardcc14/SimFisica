

class MenuManager:
    def __init__ (self, levelManager):
        self.levels = []
        self.levelManager = levelManager

    def update(self):
        '''
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and scene == "menu":
                if view.level_1_button.collidepoint(pygame.mouse.get_pos()):
                    self.levelManager.loadLevel(1)
                    scene = "level"
                elif view.level_2_button.collidepoint(pygame.mouse.get_pos()):
                    self.levelManager.loadLevel(2)
                    scene = "level"
                elif view.level_3_button.collidepoint(pygame.mouse.get_pos()):
                    self.levelManager.loadLevel(3)
                    scene = "level"
        pass
        '''

    def loadLevel(self, level):
        self.levelManager.loadLevel(level)
        return