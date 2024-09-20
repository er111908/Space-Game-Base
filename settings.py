import pygame
from keybinding import Keybinding
class Settings:
    def __init__(self):
        self.screen_width = 1600
        self.screen_height = 1000
        self.background_color = (13, 10, 45)
        self.move_left_keybinding = Keybinding([pygame.K_d, pygame.K_LEFT])
        self.move_right_keybinding = Keybinding([pygame.K_d, pygame.K_RIGHT])
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = (150, 150, 150)