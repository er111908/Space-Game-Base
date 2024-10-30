from alien import Alien
import pygame
class Armada:
    def __init__(self, game):
        self.rows = 2
        self.columns = 5
        self.speed = 2
        self.moving_right = True
        self.aliens = {}
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.height = self.screen_rect.height * .6
        self.width = self.screen_rect.width * .8
        self.rect = pygame.rect.Rect(0, 0, self.width, self.height)
        
        self.rect.midtop = self.screen_rect.midtop
        self.rect.top += 20
        self.reference_alien = Alien(game)
        self.row_gutter = (self.height - self.reference_alien.rect.height * self.rows) / (self.rows - 1)
        self.column_gutter = (self.width - self.reference_alien.rect.width * self.columns) / (self.columns - 1)
        self.aliens = {i: Alien(game) for i in range(0, self.columns * self.rows)}
        alien_index = 0
        for row_index in range(0, self.rows):
            for column_index in range(0, self.columns):
                alien_x = column_index * (self.reference_alien.rect.width + self.column_gutter)
                alien_y = row_index * (self.reference_alien.rect.height + self.row_gutter)
                alien_offset = (self.rect.topleft[0] + alien_x, self.rect.topleft[1] + alien_y)
                self.aliens[alien_index].rect.topleft = alien_offset
                alien_index += 1
    def blitme(self):
        for alien in self.aliens.values():
            alien.blitme()
    def update(self):
        if self.moving_right:
            self.rect.x += self.speed
            if self.rect.right > self.screen_rect.right:
                self.moving_right = False
        else:
            self.rect.x -= self.speed
            if self.rect.left < self.screen_rect.left:
                self.moving_right = True
        for alien in self.aliens.values():
            if self.moving_right:
                alien.rect.x += self.speed
            else:
                alien.rect.x -=self.speed