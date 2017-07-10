import pygame, Implementation.constans as constans
from pygame import *

class Entity(sprite.Sprite) :
    def __init__(self):
        sprite.Sprite.__init__(self)


class Player(sprite.Sprite) :
    def __init__(self, x, y) :
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.image = Surface((constans.PLAYER_WIDTH,
                              constans.PLAYER_HEIGHT))
        self.image.fill(Color("Green"))
        self.rect = Rect(x, y,
                         constans.PLAYER_WIDTH,
                         constans.PLAYER_HEIGHT)
        self.on_ground = False

    def update(self, left, right, up, blocks):
        if left:
            self.xvel = -constans.MOVE_SPEED

        if right:
            self.xvel = constans.MOVE_SPEED

        if not (left or right):
            self.xvel = 0

        if self.on_ground and up :
            self.yvel = -constans.MOVE_SPEED_JUMP_START
            self.on_ground = False

        self.rect.x += self.xvel
        self.collide(blocks)
        self.rect.y += self.yvel
        self.collide(blocks)

        if not self.on_ground:
            self.yvel += constans.GRAVITY

    def collide(self, blocks):
        for p in blocks:
            if self.rect.colliderect(p.rect):
                if self.xvel > 0:
                    self.rect.right = p.rect.left

                if self.xvel < 0:
                    self.rect.left = p.rect.right

                if self.yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.on_ground = True
                    self.yvel = 0

                if self.yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
