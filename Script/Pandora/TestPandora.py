import unittest
from Pandora import Pandora

class TestPandora(unittest.TestCase):
    def setUp(self):
        self.money_bag = Pandora()

    def test_collect(self):
        self.money_bag.collect("10")
        self.assertEqual(self.money_bag.get_amount(), 10)
        self.assertEqual(self.money_bag.get_money_list(), ["10"])

        self.money_bag.collect("20")
        self.assertEqual(self.money_bag.get_amount(), 30)
        self.assertEqual(self.money_bag.get_money_list(), ["10", "20"])

    def test_remove(self):
        # Remove is not used, so there are no test cases for it. :)
        pass

    def test_get_amount(self):
        self.assertEqual(self.money_bag.get_amount(), 0)

        self.money_bag.collect("10")
        self.assertEqual(self.money_bag.get_amount(), 10)

        self.money_bag.collect("20")
        self.assertEqual(self.money_bag.get_amount(), 30)

    def test_get_money_list(self):
        self.assertEqual(self.money_bag.get_money_list(), [])

        self.money_bag.collect("10")
        self.assertEqual(self.money_bag.get_money_list(), ["10"])

        self.money_bag.collect("20")
        self.assertEqual(self.money_bag.get_money_list(), ["10", "20"])

if __name__ == "__main__":
    unittest.main()