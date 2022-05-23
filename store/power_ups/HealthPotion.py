from store.lasers.Laser import Laser, collide
import pygame

from store.power_ups.PowerUp import PowerUp

HEALTH_IMG = pygame.transform.scale(pygame.image.load(
    "assets/images/pixel-heart.png"), (30, 30))


class HealthPotion(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = HEALTH_IMG
        self.mask = pygame.mask.from_surface(self.img)
