from store.ships.AssaultShip import AssaultShip
from store.lasers.Laser import Laser
import os
import pygame

G = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "images", "green_laser.png")), (25, 25))

GREEN_LASER = pygame.transform.rotate(G, 90.0)

WIDTH, HEIGHT = (130, 110)

ASSAULT_SHIP = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets", "images", "PlayerAssault.png")), (WIDTH, HEIGHT))


class PlayerAssault(AssaultShip):
    def __init__(self, x: int, y: int, health=150):
        super().__init__(x, y, health)
        self.ship_img = ASSAULT_SHIP
        self.laser_img = GREEN_LASER
        self.maxHealth = 150
        self.mask = pygame.mask.from_surface(self.ship_img)

    def shoot(self, window):
        if self.cool_down_counter == 0:
            laser = Laser(self.x + 52.5, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    # TODO include more code from pygame
