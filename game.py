import sys

import pygame
from settings import Settings
from ship import Ship

class NotSpaceInvaders:
    """Totally *not* a reskinned version of Space Invaders.
        Also, this class manages all game assets and behavior. Just FYI.
    """

    def __init__(self):
        """Define what happens when the game starts, and also create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Definitely NOT Space Invaders")
        self.ship = Ship(self)

        self.clock = pygame.time.Clock()

    def run_game(self):
        """Here's the loop that contains the functions that runs every frame of our game."""
        while True:
            self._check_events()
            self._draw_frame()
            self.ship.move()
            self.clock.tick(60)

    def _draw_frame(self):
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()
        # Make the most-recently-drawn scene visible (Draw frame to screen)
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self.ship.is_moving_left = self._check_keydown_events(event, [pygame.K_a, pygame.K_LEFT])
            self.ship.is_moving_right = self._check_keydown_events(event, [pygame.K_d, pygame.K_RIGHT])
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.ship.is_moving_left = False

    def _check_keydown_events(self, event, keys):
        if event.type == pygame.KEYDOWN:
            key_events = [event.key == key for key in keys]
            print(key_events)
            if any(key_events):
                return True

if __name__ == '__main__':
    # Instantiate the main app class and run the game.
    nsi = NotSpaceInvaders()
    nsi.run_game()