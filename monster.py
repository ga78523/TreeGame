import pygame
import random


class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 800 + random.randint(0, 300)
        self.rect.y = 550
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 700 + random.randint(0, 300)
            self.velocity = random.randint(1, 2)
            self.health = self.max_health

    def update_health_bar(self, surface):
        bar_color = (53, 227, 211)
        back_bar_color = (10, 10, 10)
        bar_position = [self.rect.x+10, self.rect.y-20, self.health, 5]
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def move_monster(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
