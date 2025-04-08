import pygame as py
import utils

class Button:
    def __init__ (self, sprite, left, top, width, height):
        self.sprite = py.transform.scale(sprite, (width, height))
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.collideZone = py.Rect(left, top, width, height)

    def draw(self, screen):
        screen.blit(self.sprite, self.collideZone)

    def isClicked(self, mouse_pos):
        return self.collideZone.collidepoint(mouse_pos)
     



