import pygame


class CometFallEvent:
    def __init__(self):
        self.percent = 0
        self.percent_speed = 5


    def add_percent(self):
        self.percent += self.percent_speed/5

    def update_bar(self, surface):
        self.add_percent()
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        pygame.draw.rect(surface, (255, 0, 0),
                         [0, surface.get_height() - 20, self.percent * (surface.get_width() / 100), 10]
                         )
