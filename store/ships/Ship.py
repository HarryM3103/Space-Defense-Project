import pygame

from store.lasers.Laser import Laser


class Ship():

    COOLDOWN = 30
    HEIGHT = 700

    def __init__(self, x: int, y: int, health: int):
        self.x = x
        self.y = y
        self.health: int = health
        self.ship_img = None
        self.laser_img = None
        self.maxHealth = None
        self.vel = None
        self.lasers = []
        self.cool_down_counter = 0
        self.damage = 25

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(self.HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 25
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self, window):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_right(self):
        pass

    def move_left(self):
        pass
