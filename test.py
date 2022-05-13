import unittest
from store.ships.FighterShip import FighterShip
from store.ships.AssaultShip import AssaultShip
from store.ships.HeavyShip import HeavyShip


class TestShipClasses(unittest.TestCase):

    F = FighterShip(30, 30)
    A = AssaultShip(50, 90)
    H = HeavyShip(60, 85)

    def test_x_values(self):

        self.assertEqual(30, self.F.x)
        self.assertEqual(50, self.A.x)
        self.assertEqual(60, self.H.x)

    def test_y_values(self):

        self.assertEqual(30, self.F.y)
        self.assertEqual(90, self.A.y)
        self.assertEqual(85, self.H.y)

    def test_health_values(self):

        self.assertEqual(100, self.F.health)
        self.assertEqual(150, self.A.health)
        self.assertEqual(250, self.H.health)

    def test_velocities(self):

        self.assertEqual(8, self.F.vel)
        self.assertEqual(5, self.A.vel)
        self.assertEqual(3, self.H.vel)

    def test_movement(self):

        F = FighterShip(30, 30)
        A = AssaultShip(50, 90)
        H = HeavyShip(60, 85)

        F.move_up()
        F.move_left()
        F.move_left()
        F.move_down()

        self.assertEqual(30, F.y)
        self.assertEqual(14, F.x)

        A.move_right()
        A.move_right()
        A.move_down()
        A.move_down()
        A.move_up()

        self.assertEqual(60, A.x)
        self.assertEqual(85, A.y)

        H.move_left()
        H.move_left()
        H.move_left()
        H.move_right()

        self.assertEqual(54, H.x)
