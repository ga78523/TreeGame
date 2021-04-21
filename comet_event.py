import pygame
from comets import Comet

class CometFallEvent:
    def __init__(self):
        self.percent = 0
        self.percent_speed = 5
        self.all_comets = pygame.sprite.Group()

    def add_percent(self)
        self.percent += self.percent_speed/100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        self.all_comets.add(Comet())

    def attempt_fall(self):
        if self.is_full_loaded():
            print("comets fall")
            self.reset_percent()
            self.meteor_fall()

    def update_bar(self, surface):
        self.add_percent()
        self.attempt_fall()
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        pygame.draw.rect(surface, (255, 0, 0),
                         [0, surface.get_height() - 20, self.percent * (surface.get_width() / 100), 10]
                         )
