import pygame
from projectile import Projectile


class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def update_health_bar(self, surface):
        bar_color = (53, 227, 211)
        back_bar_color = (10, 10, 10)
        bar_position = [self.rect.x + 40, self.rect.y - 20, self.health, 5]
        back_bar_position = [self.rect.x + 40, self.rect.y - 20, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self, amount):
        if self.health - amount > 0:
            self.health -= amount
        else:
            self.game.game_over()

    def launch_projectile(self):
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
