from Box import Box
from StoneBox import StoneBox
from GlassBox import GlassBox
from WoodBox import WoodBox
import pygame
import Box2D as b2
import utils

class TowerJoint():
    def __init__(self, world, x, y, w, h, material):
        self.material = material
        self.images = []
        self.boxes:list[Box] = []
        self.currentStatus = 0
        self.images.append(pygame.image.load("assets/blocks/" + material + "/box/1.png"))
        self.images.append(pygame.image.load("assets/blocks/" + material + "/box/2.png"))
        self.images.append(pygame.image.load("assets/blocks/" + material + "/box/3.png"))
        self.images.append(pygame.image.load("assets/blocks/" + material + "/box/4.png"))
        
        for i in range(3):
            ypos = y + i * h
            if material == "wood":
                self.boxes.append(WoodBox(world, x, ypos, w, h, self.images))
            elif material == "stone":
                self.boxes.append(StoneBox(world, x, y, w, h, self.images))
            elif material == "glass":
                self.boxes.append(GlassBox(world, x, y, w, h, self.images))   
        
        print("BOXES:", self.boxes[-1].body.position, self.boxes[0].body.position, self.boxes[1].body.position)
        self.joints = []
        for i in range(len(self.boxes) - 1):
            joint = world.CreateWeldJoint(
                bodyA=self.boxes[i].body,
                bodyB=self.boxes[i + 1].body,
                localAnchorA=(0, (h/100) / 2),
                localAnchorB=(0, (-h/100) / 2),
                collideConnected=True
            )
            self.joints.append(joint)

    def draw(self, screen:pygame.Surface):
        for i, box in enumerate(self.boxes):
            #print("BOX DRAW:", i, "POS: ", box.body.position)
            box.draw(screen)

    def update(self,world):
        for box in self.boxes:
            box.update(world)
        

