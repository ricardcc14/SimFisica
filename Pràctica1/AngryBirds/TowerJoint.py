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
        self.boxes = []
        for i in range(3):
            ypos = y + i * h
            if material == "wood":
                self.boxes.append(WoodBox(world, x, ypos, w, h, self.images))
            elif material == "stone":
                self.boxes.append(StoneBox(world, x, ypos, w, h, self.images))
            elif material == "glass":
                self.boxes.append(GlassBox(world, x, ypos, w, h, self.images))   
        

        self.joints = []
        for i in range(len(self.boxes) - 1):
            joint = world.CreateWeldJoint(
                bodyA=self.boxes[i].body,
                bodyB=self.boxes[i + 1].body,
                localAnchorA=(0, h / 2),
                localAnchorB=(0, -h / 2),
                collideConnected=False
            )
            self.joints.append(joint)


