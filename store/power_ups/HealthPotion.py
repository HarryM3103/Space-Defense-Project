from store.lasers.Laser import Laser, collide
import pygame

HEALTH_IMG = pygame.transform.scale(pygame.image.load(
    "assets/images/pixel-heart.png"), (30, 30))


class HealthPotion():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = HEALTH_IMG
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move_down(self, vel):
        self.y += vel

    def collision(self, obj):
        return collide(self, obj)

    def get_width(self):
        return self.img.get_width()

    def get_height(self):
        return self.img.get_height()
