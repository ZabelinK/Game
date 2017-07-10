import pygame, Implementation.constans
from pygame import *

class Block(sprite.Sprite) :
    def __init__(self, sym, x, y, face) :
        self.x = x
        self.y = y
        self.sym = sym
        self.face = face

    def draw(self):
        if self.sym == '#':
            pygame.draw.rect(self.face, Color("Red"), Rect(self.x, self.y,
                                                  Implementation.constans.BLOCK_HEIGHT,
                                                  Implementation.constans.BLOCK_WIDTH))