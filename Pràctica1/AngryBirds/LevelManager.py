import utils
import pygame
import Box2D as b2
from Bird import Bird
from Box import Box
from Circle import Circle
from Pig import Pig
from Surface import Surface
from ContactListener import ContactListener

class LevelManager:


    def __init__ (self, screen):
        self.levels_json = utils.readJson("levels.json")
        self.screen = screen


        self.frames = 60
        # Box2D
        self.world = b2.b2World()
        self.time_step = 1/self.frames
        self.vel_iters, self.pos_iters = 8, 3
        contactListener = ContactListener()
        self.world.contactListener = contactListener

        self.birds:list[Bird] = []
        self.boxes:list[Box] = []
        self.circles:list[Circle] = []
        self.pigs:list[Pig] = []


        self.basicBird = []
        self.basicBird.append(pygame.image.load("assets/BasicBird.png"))
        self.basicBird.append(pygame.image.load("assets/BasicBirdCollided.png"))
        self.basicBird.append(pygame.image.load("assets/BasicBirdDisappear.png"))

        self.bkgSky = pygame.image.load("assets/sky.png")
        self.bkgFloor = pygame.image.load("assets/floor.png")

        self.surface = Surface(self.world, self.screen.get_width()/2, 100, self.screen.get_width()*2, 5)

    def loadLevel(self, level):


        # birds.append(Bird(world, 300, 300, 25, basicBird))

        self.boxes.append(Box(self.world, 0, 200, 100, 100, None, "wood"))
        self.boxes.append(Box(self.world, 1000, 300, 100, 100, None, "wood"))
        self.boxes.append(Box(self.world, 1000, 400, 100, 100, None, "wood"))

        self.pigs.append(Pig(self.world, 1000, 500, 50, None))
                    
                    
    def runLevel(self, scene):
        # fill the screen with a color to wipe away anything from last frame
        self.screen.fill("gray")
        

        # RENDER YOUR GAME HERE
        self.world.Step(self.time_step, self.vel_iters, self.pos_iters)


        
    
    def draw(self):
        utils.drawRotatedImage(self.screen, self.bkgSky, b2.b2Vec2(self.screen.get_width()/2, self.screen.get_height()/2), self.screen.get_width(), self.screen.get_height(), 0)
        utils.drawRotatedImage(self.screen, self.bkgFloor, b2.b2Vec2(self.screen.get_width()/2, self.screen.get_height()/2+45), self.screen.get_width(), self.screen.get_height(), 0)

        #if(mouse_pressed): pygame.draw.line(self.screen, "crimson", origin, pygame.mouse.get_pos())

        for i, bird in enumerate(self.birds):
            if(bird.isRemoved):
                self.birds.pop(i)
            else:
                bird.update(self.world)
                bird.draw(self.screen)

        for i, box in enumerate(self.boxes):
            if(box.isRemoved):
                self.boxes.pop(i)
            else:
                box.update()
                box.draw(self.screen)
        
        for i, pig in enumerate(self.pigs):
            if(pig.isRemoved):
                self.pigs.pop(i)
            else:
                pig.update(self.world)
                pig.draw(self.screen)

        self.surface.draw(self.screen)
        pass

    def throwBird(self, origin, end):
        direction = origin - end

        self.birds.append(Bird(self.world, origin.x, self.screen.get_height()-origin.y, 25, self.basicBird))
        self.birds[-1].setLinearVelocity(direction.x, -direction.y)
        pass