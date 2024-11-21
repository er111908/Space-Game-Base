import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet, EnemyBullet
from alien import Alien
from armada import Armada
import random

class NotSpaceInvaders:
    """Totally *not* a reskinned version of Space Invaders.
        Also, this class manages all game assets and behavior. Just FYI.
    """

    def __init__(self):
        """Define what happens when the game starts, and also create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("cat vs dog")
        pygame.mixer.init()
        self.ship = Ship(self)
        self.armada = Armada(self)
        self.bullets = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.BULLET_EVENT = pygame.USEREVENT + 1
        self.ENEMY_BULLET_EVENT = self.BULLET_EVENT + 1
        self.cheese_sound = pygame.mixer.Sound("assets/catbark.mp3")
        self.background_music = pygame.mixer.Sound("assets/csgo.mp3")
        self.dogbark = pygame.mixer.Sound("assets/dogbark.mp3")
        self.background_music.play()
        pygame.time.set_timer(self.ENEMY_BULLET_EVENT, 500)
        self.LOSE_EVENT = pygame.ENEMY_BULLET_EVENT + 1
        self.WIN_EVENT = self.LOSE_EVENT + 1

    def run_game(self):
        """Here's the loop that contains the functions that runs every frame of our game."""
        while True:
            self._check_events()
            self._check_hitboxes()
            self._draw_frame()
            self.bullets.update()
            self.ship.update()
            self.armada.update()
            self.clock.tick(self.settings.max_fps)

    def _draw_frame(self):
        self.screen.fill(self.settings.background_color)
        self.ship.blitme()
        self.armada.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most-recently-drawn scene visible (Draw frame to screen)
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #print("Is ship moving?" + str(self.ship.is_moving_left))
            #print("Is ship moving?" + str(self.ship.is_moving_right))
            
            # Keydown Events
            if self._check_keydown_events(event, self.settings.move_left_keybinding):
                self.ship.is_moving_left = True
                
            elif self._check_keydown_events(event, self.settings.move_right_keybinding):
                self.ship.is_moving_right = True
            
            if self._check_keydown_events(event, self.settings.fire_bullet_keybinding):
                pygame.time.set_timer(self.BULLET_EVENT, 1000 // self.settings.bullet_fire_rate)

            # Keyup Events
            if self._check_keyup_events(event, self.settings.move_left_keybinding):
                self.ship.is_moving_left = False

            if self._check_keyup_events(event, self.settings.move_right_keybinding):
                self.ship.is_moving_right = False

            if self._check_keyup_events(event, self.settings.fire_bullet_keybinding):
                pygame.time.set_timer(self.BULLET_EVENT, 0)

            if event.type == self.BULLET_EVENT:
                self._fire_bullet()

            if event.type == self.ENEMY_BULLET_EVENT:
                self._fire_enemy_bullet(Alien)

    def _check_keydown_events(self, event, keybinding):
        if event.type == pygame.KEYDOWN:
            key_events = [event.key == key for key in keybinding.keys]
            if any(key_events):
                #print("Key pressed: " + str(event.key))
                return True
            
    def _check_keyup_events(self, event, keybinding):
        if event.type == pygame.KEYUP:
            key_events = [event.key == key for key in keybinding.keys]
            if any(key_events):
                #print("Key depressed: " + str(event.key))
                return True
            
    def _fire_bullet(self):
        """Create a new bullet and add it to our group of bullet sprites"""
        new_bullet = Bullet(self)
        new_bullet.image = pygame.transform.scale(new_bullet.image, (new_bullet.rect.width * .3, new_bullet.rect.height * .3))
        self.bullets.add(new_bullet)
        self.cheese_sound.stop()
        self.cheese_sound.play()

    def _fire_enemy_bullet(self, alien):
        random_index = random.randint(0, len(self.armada.aliens) - 1)
        _, alien = list(self.armada.aliens.items())[random_index]
        new_bullet = EnemyBullet(self, alien)
        self.bullets.add(new_bullet)
        self.dogbark.stop()
        self.dogbark.play()

    def _check_hitboxes(self):
        for bullet in self.bullets.sprites():
            if type(bullet) == Bullet:
                collisions = bullet.rect.collidedict(self.armada.aliens, 1)
                if collisions:
                    del self.armada.aliens[collisions[0]]
                    bullet.kill()
            if type(bullet) == EnemyBullet:
                collision = bullet.rect.colliderect(self.ship.rect)
                if collision:
                    self.ship.lives -= 1
                    .

if __name__ == '__main__':
    # Instantiate the main app class and run the game.
    nsi = NotSpaceInvaders()
    nsi.run_game()