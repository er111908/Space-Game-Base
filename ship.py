import pygame

class Ship:
    """A class to manage the ship"""
    
    def __init__(self, game):
        """Initialize the ship and set initial position"""

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.game = game

        self.image = pygame.image.load('assets/my_spaceship_small.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom middle of screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.is_moving_left = False
        self.is_moving_right = False

    def update(self):
        if self.is_moving_left:
            #print("moving left")
            self.rect.x -= 1
        if self.is_moving_right:
            #print("moving right")
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image, self.rect)