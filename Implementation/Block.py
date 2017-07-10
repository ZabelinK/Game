import pygame, Implementation.constans as constans
from pygame import *

class Block(sprite.Sprite) :
    def __init__(self, sym, x, y) :
        sprite.Sprite.__init__(self)
        self.image = Surface((constans.BLOCK_WIDTH, constans.BLOCK_HEIGHT))
        if sym == '#':
            self.image.fill(Color("Red"))
        self.rect = Rect(x, y, constans.BLOCK_WIDTH, constans.BLOCK_HEIGHT)
