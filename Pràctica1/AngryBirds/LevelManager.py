import utils
import pygame
import numpy
import Box2D as b2
from Bird import Bird
from Red import Red
from Big import Big
from Box import Box
from WoodBox import WoodBox
from GlassBox import GlassBox
from StoneBox import StoneBox
from IndestructibleBox import IndestructibleBox
from TowerJoint import TowerJoint
from ComplexJoint import ComplexJoint
from Circle import Circle
from Pig import Pig
from Surface import Surface
from ContactListener import ContactListener
from PointsManager import PointsManager

class LevelManager:


    def __init__ (self, screen, pointsManager):
        self.levels_json = utils.readJson("levels.json")
        self.screen = screen
        self.pointsManager = pointsManager

        self.frames = 60
        # Box2D
        self.world = b2.b2World()
        self.time_step = 1/self.frames
        self.vel_iters, self.pos_iters = 8, 3
        contactListener = ContactListener(self.pointsManager)
        self.world.contactListener = contactListener

        #GESTIÓ D'ESTATS DEL NIVELL
        self.STATE_NO_BIRD_SELECTED = 0
        self.STATE_BIRD_SELECTED = 1
        self.STATE_CHARGING = 2
        self.STATE_BIRD_FLYING = 3
        self.levelState = self.STATE_NO_BIRD_SELECTED

        self.slingshotSprites = [pygame.image.load("assets/catapult/slingshotBack.png"), pygame.image.load("assets/catapult/slingshotFront.png")]
        self.catapult_origin = b2.b2Vec2(195, 230)
        self.origin = b2.b2Vec2(195, 230)
        self.end = b2.b2Vec2(0, 0)
        self.mouse_pressed = False

        self.birds:list[Bird] = []
        # Area de selecció d'ocells
        self.bird_area = []
        self.bird_slot_size = (50, 50)
        self.bird_slot_spacing = 60
        # LLista amb els ocells diponibles
        self.birdsAvailable:list = []
        # Llista amb el sprite l'ocell seleccionat
        self.currentBirdSprite = []
        self.selectedBirdIndex = None
        self.boxes:list[Box] = []
        self.towerJoints:list[TowerJoint] = []
        self.complexJoints:list[ComplexJoint] = []
        self.circles:list[Circle] = []
        self.pigs:list[Pig] = []

        self.bkgSky = pygame.image.load("assets/sky.png")
        self.bkgFloor = pygame.image.load("assets/floor.png")

        self.surface = Surface(self.world, self.screen.get_width()/2, 100, self.screen.get_width()*2, 5)

    def loadLevel(self, level_id):

        #Llegir informació del JSON
        level_data = []
        data = utils.readJson('levels.json')
        for i, level in enumerate(data):
            if (i == level_id -1):
                level_data = level
                break

        #Esborrar assets en memòria
        self.birdsAvailable.clear()
        self.pigs.clear()
        self.boxes.clear()
        self.circles.clear()
        self.birds.clear()
        self.towerJoints.clear()
        self.complexJoints.clear()
            
        
        #Load Birds
        for bird in level_data["birds"]:
            bird_path = f"assets/birds/{bird}/bird_{bird}.png"
            self.birdsAvailable.append(bird_path) 
        #Load Pigs
        pigs_data = level_data.get("pigs", [])
        for (pig_type, pig_info) in pigs_data.items():

            pigSprites = []
            pigSprites.append(pygame.image.load("assets/pigs/" + pig_type + "/1.png"))
            pigSprites.append(pygame.image.load("assets/pigs/" + pig_type + "/2.png"))
            pigSprites.append(pygame.image.load("assets/pigs/" + pig_type + "/3.png"))

            pig_type = pigs_data["basic"]

            for single_pig in pig_type:
                pig = Pig(self.world, single_pig["x"], single_pig["y"], single_pig["r"], pigSprites)
                self.pigs.append(pig)
        
        
        #Load Structures
        for structure in level_data["blocks"]:
            material = structure["material"]
            type = structure["type"]
            
            
            if type == "box":
                if material == "indestructible":
                    box = IndestructibleBox(self.world, structure["x"], structure["y"], structure["w"], structure["h"])
                else:
                    blockSprites = []
                    blockSprites.append(pygame.image.load("assets/blocks/" + material + "/" + type + "/1.png"))
                    blockSprites.append(pygame.image.load("assets/blocks/" + material + "/" + type + "/2.png"))
                    blockSprites.append(pygame.image.load("assets/blocks/" + material + "/" + type + "/3.png"))
                    blockSprites.append(pygame.image.load("assets/blocks/" + material + "/" + type + "/4.png"))
                    if material == "wood":
                        box = WoodBox(self.world, structure["x"], structure["y"], structure["w"], structure["h"], blockSprites)
                    elif material == "stone":
                        box = StoneBox(self.world, structure["x"], structure["y"], structure["w"], structure["h"], blockSprites)
                    elif material == "glass":
                        box = GlassBox(self.world, structure["x"], structure["y"], structure["w"], structure["h"], blockSprites)
                        
                    else:
                        box = Box(self.world, structure["x"], structure["y"], structure["w"], structure["h"], blockSprites)
                
                # Configurar angle si existeix
                if "angle" in structure:
                    box.body.angle = numpy.radians(structure["angle"])
                
                self.boxes.append(box)

            elif type == "tower":
                joint = TowerJoint(self.world, structure["x"], structure["y"], structure["w"], structure["h"], material)
                self.towerJoints.append(joint)
            elif type == "complex":
                joint = ComplexJoint(self.world, structure["x"], structure["y"], structure["w"], structure["h"], material)
                self.complexJoints.append(joint)

        #Load birds areas
        self.bird_area = []
        for i in range(len(self.birdsAvailable)):
            x = self.bird_slot_size[0] + i * self.bird_slot_spacing
            y = self.bird_slot_size[1]
            self.bird_area.append(pygame.Rect(x, y, self.bird_slot_size[0], self.bird_slot_size[1]))
 
        #Points system
        points_thresh_3starts = level_data["points"]["3stars"]
        points_thresh_2stars = level_data["points"]["2stars"]
        points_thresh_1star = level_data["points"]["1star"]
        self.pointsManager.restartLevel(level_id-1, len(self.pigs), points_thresh_1star, points_thresh_2stars, points_thresh_3starts)

        return True
                    
                    
    def runLevel(self):
        # RENDER YOUR GAME HERE
        self.world.Step(self.time_step, self.vel_iters, self.pos_iters)
        

        
    
    def draw(self):
        
        utils.drawRotatedImage(self.screen, self.bkgSky, b2.b2Vec2(self.screen.get_width()/2, self.screen.get_height()/2), self.screen.get_width(), self.screen.get_height(), 0)
        utils.drawRotatedImage(self.screen, self.bkgFloor, b2.b2Vec2(self.screen.get_width()/2, self.screen.get_height()/2+45), self.screen.get_width(), self.screen.get_height(), 0)

        #if(mouse_pressed): pygame.draw.line(self.screen, "crimson", origin, pygame.mouse.get_pos())
        utils.drawRotatedImage(self.screen, self.slingshotSprites[0], b2.b2Vec2(200, 415), 34, 160, 0)
       
        for i, bird_img in enumerate(self.birdsAvailable):
        # Dibuixar el slot (opcional)
            pygame.draw.rect(self.screen, (200, 200, 200, 128), self.bird_area[i], 2)
              
            bird_sprite = pygame.image.load(bird_img)
            # Escalar l'ocell perquè encaixi al slot si cal
            if bird_sprite.get_size() != self.bird_slot_size:
                bird_sprite = pygame.transform.scale(bird_sprite, self.bird_slot_size)
            self.screen.blit(bird_sprite, self.bird_area[i])
            
        
        if self.levelState == self.STATE_BIRD_SELECTED:
            self.screen.blit(self.currentBirdSprite[0], (self.catapult_origin.x-25, self.screen.get_height()-self.catapult_origin.y-25))
        elif self.levelState == self.STATE_CHARGING:
            mouse_pos = pygame.mouse.get_pos()
            direction = pygame.math.Vector2(self.origin) - pygame.math.Vector2(mouse_pos)

            max_length = 200
            if direction.length() > max_length:
                direction.scale_to_length(max_length)

            limited_mouse_pos = (self.origin[0] - direction.x, self.origin[1] - direction.y)
            pygame.draw.line(self.screen, "crimson", self.origin, limited_mouse_pos)

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
                box.update(self.world)
                box.draw(self.screen)
        for i, joint in enumerate(self.towerJoints):
            joint.draw(self.screen)
            joint.update(self.world)
        for i, joint in enumerate(self.complexJoints):
            joint.draw(self.screen)
            joint.update(self.world)
        for i, pig in enumerate(self.pigs):
            if(pig.isRemoved):
                self.pigs.pop(i)
            else:
                pig.update(self.world)
                pig.draw(self.screen)

        utils.drawRotatedImage(self.screen, self.slingshotSprites[1], b2.b2Vec2(180, 385), 34, 99, 0)
        self.surface.draw(self.screen)
        pass

    def throwBird(self, origin, end):
        direction = origin - end

        max_launch_force = 200 

        if direction.length > max_launch_force:
            direction.Normalize()
            direction *= max_launch_force
        if self.birdsAvailable[self.selectedBirdIndex] == "assets/birds/big/bird_big.png":
            self.birds.append(Big(self.world, 190, self.screen.get_height()-370, self.currentBirdSprite))
            
        else:
            self.birds.append(Red(self.world, 190, self.screen.get_height()-370, self.currentBirdSprite))
        self.birds[-1].setLinearVelocity(direction.x, -direction.y)
        self.birdsAvailable.pop(self.selectedBirdIndex)
        self.selectedBirdIndex = None
        self.levelState = self.STATE_BIRD_FLYING
        self.levelState = self.STATE_NO_BIRD_SELECTED
        pass

    def handleMouseDown(self, mouse_pos):
        print("MouseDown")
        if (self.levelState == self.STATE_NO_BIRD_SELECTED and self.birds == []) or (self.levelState == self.STATE_NO_BIRD_SELECTED and self.birds[-1].body.position.x >= 12) or (self.levelState == self.STATE_NO_BIRD_SELECTED and self.birds[-1].body.position.x < 0):
            
            print(self.birdsAvailable)
            for i, area in enumerate(self.bird_area):
                if area.collidepoint(mouse_pos):
                    self.currentBirdSprite.clear()
                    self.currentBirdSprite.append(pygame.image.load(self.birdsAvailable[i]))
                    self.currentBirdSprite.append(pygame.image.load(self.birdsAvailable[i].replace(".png", "_collided.png")))
                    self.currentBirdSprite.append(pygame.image.load(self.birdsAvailable[i].replace(".png", "_disappear.png")))
                    self.selectedBirdIndex = i
                    self.levelState = self.STATE_BIRD_SELECTED
                    return
                
        elif self.levelState == self.STATE_BIRD_SELECTED:
            print("Bird selected: Near catapulta", self.nearCatapult(mouse_pos))

            if self.nearCatapult(mouse_pos):
                self.levelState = self.STATE_CHARGING
                self.origin = b2.b2Vec2(mouse_pos)
                self.mouse_pressed = True

            else :
                for i, area in enumerate(self.bird_area):
                    if area.collidepoint(mouse_pos):
                        self.currentBirdSprite.clear()
                        self.currentBirdSprite.append(pygame.image.load(self.birdsAvailable[i]))
                        self.currentBirdSprite.append(pygame.image.load(self.birdsAvailable[i].replace(".png", "_collided.png")))
                        self.currentBirdSprite.append(pygame.image.load(self.birdsAvailable[i].replace(".png", "_disappear.png")))
                        self.selectedBirdIndex = i
                        self.levelState = self.STATE_BIRD_SELECTED
                        return
        #elif self.levelState == self.STATE_BIRD_FLYING:
         #   if self.birds:
          #      self.birds[-1].activateHability()

    def handleMouseUp(self, mouse_pos):
        print("MouseUp")
        if self.levelState == self.STATE_CHARGING:
            self.end = b2.b2Vec2(mouse_pos)
            self.throwBird(self.origin, self.end)

            sound = pygame.mixer.Sound("assets/ui/music/flying-sound.mp3")
            sound.set_volume(0.3)  
            #sound.play()
            

    def nearCatapult(self, pos):
       
        origin_screen = (self.catapult_origin.x, self.screen.get_height() - self.catapult_origin.y)

        distance = numpy.sqrt((pos[0] - origin_screen[0])**2 + (pos[1] - origin_screen[1])**2)
        return distance < 100
    

    def destroyAllObjects(self):
        for box in self.boxes:
            box.destroy(self.world)
        for pig in self.pigs:
            pig.destroy(self.world)
        for bird in self.birds:
            bird.destroy(self.world)
        for complex in self.complexJoints:
            complex.destroy(self.world)
        for complex2 in self.towerJoints:
            complex2.destroy(self.world)



