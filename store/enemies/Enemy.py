from store.ships.Ship import Ship
import os
import pygame


WIDTH, HEIGHT = (70, 70)

B = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets", "images", "BlueEnemyShip.png")), (WIDTH, HEIGHT))

R = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets", "images", "RedEnemyShip.png")), (WIDTH, HEIGHT))

BLUE_SHIP = pygame.transform.rotate(B, 180.0)
RED_SHIP = pygame.transform.rotate(R, 180.0)
GREY_SHIP = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets", "images", "GreyEnemyShip.png")), (WIDTH, HEIGHT))

RD = pygame.transform.scale(pygame.image.load(os.path.join(
    "assets", "images", "red laser.png")), (60, 60))
RED_LASER = pygame.transform.rotate(RD, 90.0)


class Enemy(Ship):

    COLOR_MAP = {
        "blue": (BLUE_SHIP, RED_LASER),
        "red": (RED_SHIP, RED_LASER),
        "grey": (GREY_SHIP, RED_LASER)
    }

    def __init__(self, x: int, y: int, color: str, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move_down(self, vel):
        self.y += vel

    # TODO include more code from pygame
