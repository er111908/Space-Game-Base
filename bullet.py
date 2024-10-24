import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.color = self.settings.bullet_color
        #self.width = self.settings.bullet_width
        #self.height = self.settings.bullet_height
        self.speed = self.settings.bullet_speed

        self.image = pygame.image.load("assets/catattack.jpg")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (self.rect.width * .5, self.rect.height * .5))
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.speed
        self.rect.y = self.y
        if self.rect.bottom < self.screen_rect.top:
            self.kill()

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
        