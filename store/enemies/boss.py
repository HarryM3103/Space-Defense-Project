from store.lasers.Laser import Laser
from store.ships.Ship import Ship
import os
import pygame

WIDTH, HEIGHT = 750, 400

BOSS_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "images", "Mothership.png")), (WIDTH, HEIGHT))

RD = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets", "images", "red laser.png")), (60, 60))
RED_LASER = pygame.transform.rotate(RD, 90.0)


class Boss(Ship):

    def __init__(self, x: int, y: int, health=1250):
        super().__init__(x, y, health)
        self.ship_img = BOSS_IMG
        self.laser_img = RED_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.lasers = []
        self.cool_down_counter = 0

    def shoot(self, window):
        if self.cool_down_counter == 0:
            laser_1 = Laser(self.x, self.y, self.laser_img)
            laser_2 = Laser(self.x, self.y, self.laser_img)
            laser_3 = Laser(self.x, self.y, self.laser_img)
            laser_4 = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser_1)
            self.lasers.append(laser_2)
            self.lasers.append(laser_3)
            self.lasers.append(laser_4)
            self.cool_down_counter = 1

    def move_down(self, vel):
        self.y += vel

    def move_left(self, vel):
        self.x -= vel

    def move_right(self, vel):
        self.x += vel
