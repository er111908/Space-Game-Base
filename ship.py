
import pygame
class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('assets/my_spaceship_small.png')
        self.rect = self.image.get_rect()
#start new ship at bottom middle screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.is_moving_left = False
        self.is_moving_right = False

    def move(self):
        if self.is_moving_left:
            self.rect.x -= 1
        if self.is_moving_right:
            self.rect.x += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)