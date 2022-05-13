from store.ships.FighterShip import FighterShip
from store.lasers.Laser import Laser

import os
import pygame

G = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "images", "green_laser.png")), (25, 25))

GREEN_LASER = pygame.transform.rotate(G, 90.0)

WIDTH, HEIGHT = (50, 50)

FIGHTER_SHIP = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets", "images", "PlayerFighter.png")), (WIDTH, HEIGHT))


class PlayerFighter(FighterShip):
    def __init__(self, x: int, y: int, health=75):
        super().__init__(x, y, health)
        self.ship_img = FIGHTER_SHIP
        self.laser_img = GREEN_LASER
        self.maxHealth = 75
        self.mask = pygame.mask.from_surface(self.ship_img)

    def shoot(self, window):
        if self.cool_down_counter == 0:
            laser = Laser(self.x + 11, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    # TODO include more code from pygame
