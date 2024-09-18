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
        
        self.screen = pygame.display.set_mode((s))
        pygame.display.set_caption("no officer, this is not a classic arcade game from 1978")
        self.ship = Ship(self)
        self.background_color = (13, 10, 45)
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Here's the loop that contains the functions that runs every frame of our game."""
        while True:
            # Watch for mouse and keyboard events (aka interrupts)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.background_color)
            self.ship.blitme()
            # Make the most-recently-drawn scene visible (Draw frame to screen)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Instantiate the main app class and run the game.
    nsi = NotSpaceInvaders()
    nsi.run_game()