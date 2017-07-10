import pygame, Implementation.Block, Implementation.constans
from pygame import *

class Level(sprite.Sprite) :
    def __init__(self, name_world) :
        sprite.Sprite.__init__(self)
        self.screen = pygame.display.set_mode(Implementation.constans.DISPLAY)
        self.back_ground = pygame.Surface(Implementation.constans.DISPLAY)
        self.back_ground.fill(Color(Implementation.constans.BACKGROUND_COLOR))
        self.face = pygame.Surface(Implementation.constans.DISPLAY)
        file = open(name_world, 'r')
        self.text = []
        for line in file:
            self.text.append(line)

    def event(self, event):
        pass

    def draw(self) :
        self.screen.blit(self.back_ground, (0,0))
        x = 0
        y = 0
        for line in self.text :
            for symb in line :
                block = Implementation.Block.Block(symb, x, y, self.face)
                block.draw()
                x += Implementation.constans.BLOCK_WIDTH
            x = 0
            y += Implementation.constans.BLOCK_HEIGHT
        self.screen.blit(self.face, (0,0))

