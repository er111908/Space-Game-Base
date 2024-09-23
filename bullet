import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.color = self.settings.bullet_color
        self.width = self.settings.bullet_width
        self.height = self.settings.bullet_height
        self.speed = self.settings.bullet_speed

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        