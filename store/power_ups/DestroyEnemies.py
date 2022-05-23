import pygame
from store.power_ups.PowerUp import PowerUp

SKULL_IMG = pygame.transform.scale(pygame.image.load(
    "assets/images/pixel-skull.png"), (30, 30))


class DestroyEnemies(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = SKULL_IMG
        self.mask = pygame.mask.from_surface(self.img)

# TODO: WORK IN PROGRESS
