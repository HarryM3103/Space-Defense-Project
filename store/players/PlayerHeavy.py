from store.ships.HeavyShip import HeavyShip
from store.lasers.Laser import Laser

import os
import pygame

G = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "images", "green_laser.png")), (25, 25))

GREEN_LASER = pygame.transform.rotate(G, 90.0)

WIDTH, HEIGHT = (175, 175)

HEAVY_SHIP = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets", "images", "PlayerHeavy.png")), (WIDTH, HEIGHT))


class PlayerHeavy(HeavyShip):
    def __init__(self, x: int, y: int, health=250):
        super().__init__(x, y, health)
        self.ship_img = HEAVY_SHIP
        self.laser_img = GREEN_LASER
        self.maxHealth = 250
        self.mask = pygame.mask.from_surface(self.ship_img)

    def shoot(self, window):
        if self.cool_down_counter == 0:
            laser_left = Laser(self.x + 52.5, self.y, self.laser_img)
            laser_right = Laser(self.x + 100, self.y, self.laser_img)
            self.lasers.append(laser_left)
            self.lasers.append(laser_right)
            self.cool_down_counter = 1

    # TODO include more code from pygame
