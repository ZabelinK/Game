import pygame, Implementation.Block as block, Implementation.Entity as entity, Implementation.constans as constans
from pygame import *

class Level(sprite.Sprite) :
    def __init__(self, name_world) :
        sprite.Sprite.__init__(self)
        self.screen = pygame.display.set_mode(constans.DISPLAY)
        self.back_ground = pygame.Surface(constans.DISPLAY)
        self.back_ground.fill(Color(constans.BACKGROUND_COLOR))
        self.player = entity.Player(300, 30)
        self.entities = pygame.sprite.Group()
        self.entities.add(self.player)
        self.blocks = []
        file = open(name_world, 'r')
        x = 0
        y = 0
        for line in file :
            for sym in line :
                if sym != '.' :
                    block_ = block.Block(sym, x, y)
                    self.blocks.append(block_)
                    self.entities.add(block_)
                x += constans.BLOCK_WIDTH
            x = 0
            y += constans.BLOCK_HEIGHT

        print("init")

    def event(self, keys):
        left = right = up = False
        if keys[K_LEFT]:
            left = True
        if keys[K_RIGHT]:
            right = True
        if keys[K_UP]:
            up = True

        self.player.update(left, right, up, self.blocks)

    def draw(self):
        self.player.update(False, False, False, self.blocks)
        self.screen.blit(self.back_ground, (0,0))
        self.entities.draw(self.screen)
