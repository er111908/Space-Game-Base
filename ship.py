import pygame

class Ship:
    """A class to manage the ship"""
    
    def __init__(self, game):
        """Initialize the ship and set initial position"""

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.game = game

        self.image = pygame.image.load('assets/cat4.png')

        # Start each new ship at the bottom middle of screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.is_moving_left = False
        self.is_moving_right = False
        pygame.transform.scale(self.image, (self.rect.width * .5, self.rect.height * .5))
        self.rect = self.image.get_rect()

    def update(self):
        if self.is_moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.game.settings.ship_speed
        if self.is_moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.game.settings.ship_speed

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)