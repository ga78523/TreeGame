from player import Player
from monster import Monster
from comet_event import CometFallEvent
import pygame


class Game:

    def __init__(self):
        self.is_playing = True
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent()
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # create and replace another the sprite's group
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.comet_event.percent = 0

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def update(self, screen):
        # apply the player and the health bar
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        # display the game bar
        self.comet_event.update_bar(screen)

        # display the projectile group on the screen
        self.player.all_projectiles.draw(screen)

        # display the monsters
        self.all_monsters.draw(screen)

        # for each projectile in the group, move the projectile
        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            monster.move_monster()
            monster.update_health_bar(screen)

        # move the player
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1080:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
