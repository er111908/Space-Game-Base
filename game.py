import sys

import pygame

class NotSpaceInvaders:
    """Totally *not* a reskinned version of Space Invaders.
        Also, this class manages all game assets and behavior. Just FYI.
    """

    def __init__(self):
        """Define what happens when the game starts, and also create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Definitely NOT Space Invaders")

    def run_game(self):
        """Here's the loop that contains the functions that runs every frame of our game."""
        while True:
            # Watch for mouse and keyboard events (aka interrupts)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most-recently-drawn scene visible (Draw frame to screen)
            pygame.display.flip()

if __name__ == '__main__':
    # Instantiate the main app class and run the game.
    nsi = NotSpaceInvaders()
    nsi.run_game()