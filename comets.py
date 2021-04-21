import pygame
import random


class Comet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 4)
        self.rect.x = random.randint(20, 800)

    def fall(self):
        self.rect.y += self.velocity
