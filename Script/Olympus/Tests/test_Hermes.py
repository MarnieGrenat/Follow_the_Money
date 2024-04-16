import unittest
from Script.Olympus.Hermes import Hermes

class HermesTest(unittest.TestCase):
    def setUp(self):
        self.hermes = Hermes("map.txt")

    def test_change_direction_horizontal(self):
        self.hermes.position = [0, 0]
        self.hermes.direction = self.hermes._RIGHT
        new_direction = self.hermes.get_curve_direction()
        self.assertEqual(new_direction, self.hermes._UPWARDS)

    def test_change_direction_vertical(self):
        self.hermes.position = [0, 0]
        self.hermes.direction = self.hermes._DOWNWARDS
        new_direction = self.hermes.get_curve_direction()
        self.assertEqual(new_direction, self.hermes._LEFT)

    def test_collect_money(self):
        self.hermes.position = [0, 0]
        self.hermes.direction = self.hermes._RIGHT
        money_list = self.hermes.collect_money()
        self.assertEqual(money_list, [1, 0])

    def test_travel_until_curve(self):
        self.hermes.position = [0, 0]
        self.hermes.direction = self.hermes._RIGHT
        money_list = self.hermes.travel_until_curve()
        self.assertEqual(money_list, [1, 0])

if __name__ == '__main__':
    unittest.main()