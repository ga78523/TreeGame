import pygame


class cometFallEvent:
    def __init__(self):
        self.percent = 0

    def add_percent(self):
        self.percent += 1

    def update_bar(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), [0, surface.get_height(), surface.get_width(), 10])
