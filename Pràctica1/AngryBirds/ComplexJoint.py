from Box import Box
from StoneBox import StoneBox
from GlassBox import GlassBox
from WoodBox import WoodBox
import pygame
import Box2D as b2
import utils

class ComplexJoint():
    def __init__(self, world, x, y, w, h, material):
        self.material = material
        self.images = []
        self.boxes:list[Box] = []
        self.grid = []
        self.joints = []
        self.currentStatus = 0
        self.images.append(pygame.image.load("assets/blocks/" + material + "/box/1.png"))
        self.images.append(pygame.image.load("assets/blocks/" + material + "/box/2.png"))
        self.images.append(pygame.image.load("assets/blocks/" + material + "/box/3.png"))
        self.images.append(pygame.image.load("assets/blocks/" + material + "/box/4.png"))
        
        pattern = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
            [1, 0, 1],
        ]
        for row_index, row in enumerate(pattern):
            box_row = []
            for col_index, has_block in enumerate(row):
                if has_block:
                    xpos = x + col_index * w 
                    ypos = y + row_index * h
                    if material == "wood":
                        box = WoodBox(world, xpos, ypos, w, h, self.images)
                    elif material == "stone":
                        box = StoneBox(world, xpos, ypos, w, h, self.images)
                    elif material == "glass":
                        box = GlassBox(world, xpos, ypos, w, h, self.images)
                    box_row.append(box)
                    self.boxes.append(box)
                else:
                    box_row.append(None)
            self.grid.append(box_row)

        # Connectem verticalment amb weld joints si hi ha blocs un damunt de l’altre
        for row_index in range(len(self.grid)):
            for col_index in range(len(self.grid[row_index])):
                current = self.grid[row_index][col_index]
                if current is None:
                    continue

                # WeldJoint amb el bloc de sota
                if row_index + 1 < len(self.grid):
                    below = self.grid[row_index + 1][col_index]
                    if below is not None:
                        joint = world.CreateWeldJoint(
                            bodyA=current.body,
                            bodyB=below.body,
                            localAnchorA=(0, -h / 200),  # h/100 perquè metres, /2 perquè mig bloc
                            localAnchorB=(0, h / 200),
                            collideConnected=False
                        )
                        self.joints.append(joint)

                # WeldJoint amb el bloc de la dreta
                if col_index + 1 < len(self.grid[row_index]):
                    right = self.grid[row_index][col_index + 1]
                    if right is not None:
                        joint = world.CreateWeldJoint(
                            bodyA=current.body,
                            bodyB=right.body,
                            localAnchorA=(w / 200, 0),
                            localAnchorB=(-w / 200, 0),
                            collideConnected=False
                        )
                        self.joints.append(joint)

    def draw(self, screen:pygame.Surface):
        for i, box in enumerate(self.boxes):
            #print("BOX DRAW:", i, "POS: ", box.body.position)
            box.draw(screen)

    def update(self,world):
        for box in self.boxes:
            box.update(world)