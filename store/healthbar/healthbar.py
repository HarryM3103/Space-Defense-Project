import pygame
from store.ships.Ship import Ship


class HealthBar:

    def __init__(self, x, y, player: Ship) -> None:
        self.x = x
        self.y = y
        self.player = player

    def draw(self, window):
        # TODO Finish creating draw method
