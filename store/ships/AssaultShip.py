from store.ships.Ship import Ship
import pygame
import os


class AssaultShip(Ship):

    VEL = 5.5
    WIDTH = 60
    HEIGHT = 60
    GAME_HEIGHT = 700

    def __init__(self, x: int, y: int, health=150):
        super().__init__(x, y, health)
        self.vel = self.VEL

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(self.GAME_HEIGHT):
                if laser in self.lasers:
                    self.lasers.remove(laser)
                else:
                    print("Okay!")
            else:
                for obj in objs:
                    if laser.collision(obj):
                        if laser in self.lasers:
                            objs.remove(obj)
                            self.lasers.remove(laser)
                        else:
                            print("Okay!")

    def move_up(self):
        self.y -= self.VEL

    def move_down(self):
        self.y += self.VEL

    def move_right(self):
        self.x += self.VEL

    def move_left(self):
        self.x -= self.VEL

    # TODO include more code for lasers, etc
