import pygame
from store.enemies.boss import Boss
from store.ships.Ship import Ship


class HealthBar:

    def __init__(self, x, y, ship: Ship, shield_color, base_color, health_color) -> None:
        self.x = x
        self.y = y
        self.ship = ship
        self.base_color = base_color
        self.health_cover = health_color
        self.shield_color = shield_color

    # TODO Create a SHIELD BAR

    def draw_healthBar(self, window):

        base_rect = pygame.Rect(
            self.x, self.y, self.ship.maxHealth, 15)
        health_rect = pygame.Rect(
            self.x, self.y, self.ship.health, 15)

        pygame.draw.rect(
            window, self.base_color, base_rect)
        pygame.draw.rect(
            window, self.health_cover, health_rect)

    def draw_shieldBar(self, window):

        shield_rect = pygame.Rect(self.x, self.y-4, self.ship.shield, 10)
        pygame.draw.rect(window, self.shield_color, shield_rect)
