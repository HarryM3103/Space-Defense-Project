from store.lasers.Laser import Laser
from store.ships.Ship import Ship
import os
import pygame

WIDTH, HEIGHT = 750, 400

BOSS_IMG = pygame.transform.scale(pygame.image.load(
    os.path.join("assets", "images", "Mothership.png")), (WIDTH, HEIGHT))

RD = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets", "images", "red laser.png")), (60, 60))

YL = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets", "images", "yellow_laser.png")), (60, 60))
RED_LASER = pygame.transform.rotate(RD, 90.0)

YELLOW_LASER = pygame.transform.rotate(RD, 90.0)


class Boss(Ship):

    GAME_HEIGHT, GAME_WIDTH = 700, 1000
    VEL = 0.5

    def __init__(self, x: int, y: int, health=850, shield=850):
        super().__init__(x, y, health)
        self.ship_img = BOSS_IMG
        self.laser_img = RED_LASER
        self.super_laser_img = YELLOW_LASER
        self.super_lasers = []
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.shield = shield
        self.maxShieldHP = 850
        self.maxHealth = 850
        self.currentHealth = 850
        self.vel = self.VEL
        self.move_counter = 0
        self.counter = 0

    def shoot_1(self, window):
        if self.cool_down_counter == 0:
            laser_1 = Laser(self.x+100, self.y+300, self.laser_img)
            self.lasers.append(laser_1)
            self.cool_down_counter = 1

    def shoot_2(self, window):
        if self.cool_down_counter == 0:
            laser_2 = Laser(self.x+225, self.y+300, self.laser_img)
            self.lasers.append(laser_2)
            self.cool_down_counter = 1

    def shoot_3(self, window):
        if self.cool_down_counter == 0:
            laser_3 = Laser(self.x+490, self.y+300, self.laser_img)
            self.lasers.append(laser_3)
            self.cool_down_counter = 1

    def shoot_4(self, window):
        if self.cool_down_counter == 0:
            laser_4 = Laser(self.x+600, self.y+300, self.laser_img)
            self.lasers.append(laser_4)
            self.cool_down_counter = 1

    def rand_shoot(self, window, num):
        if num == 1:
            self.shoot_1(window)
        if num == 2:
            self.shoot_2(window)
        if num == 3:
            self.shoot_3(window)
        if num == 4:
            self.shoot_4(window)

    def move_down(self):
        self.y += self.vel

    def move_left(self):
        self.x -= self.vel

    def move_right(self):
        self.x += self.vel

    def move_side_to_side(self):
        self.move_counter += 1
        self.x += self.vel
        if self.move_counter >= 400:
            self.vel *= -1
            self.move_counter = 0

    def shield_regen(self):
        self.counter += 2
        self.shield += 2
        if self.counter >= 850:
            self.currentHealth = self.health
            self.counter = 0

    def checkBorder_LEFT(self) -> bool:
        if self.x - self.vel == 0:
            return True
        return False

    def checkBorder_RIGHT(self) -> bool:
        if self.x + self.vel + self.get_width() < self.GAME_WIDTH:
            return True
        return False

    def checkBorder_UP(self) -> bool:
        if self.y - self.vel > 0:
            return True
        return False

    def checkBorder_DOWN(self) -> bool:
        if self.y + self.vel + self.get_width() < self.GAME_HEIGHT:
            return True
        return False
