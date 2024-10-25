from alien import Alien
import pygame
class Armada:
    def __init__(self, game):
        self.rows = 3
        self.columns = 3
        self.aliens = {}
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.height = self.screen_rect.height * .6
        self.width = self.screen_rect.width * .8
        self.rect = pygame.rect.Rect(0, 0, self.width, self.height)
        self.rect.midtop = self.screen_rect.midtop
        self.rect.top += 20
        self.reference_alien = Alien()
        self.row_gutter = (self.height - self.reference_alien.rect.height * self.rows) / (self.rows - 1)
        self.column_gutter = (self.width - self.reference_alien.rect.width * self.columns) / (self.columns - 1)
        self.aliens = {i: Alien() for i in range(0, self.columns * self.rows)}
        column_index = 0
        for alien in self.aliens:
            for j in range(0, self.rows):
                column_index += 1
                if column_index > self.columns:
                    