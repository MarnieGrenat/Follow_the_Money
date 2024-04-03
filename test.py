import unittest
from script import main

class TestScript(unittest.TestCase):
    def test_caseG01(self):
        expected_total_money = 104
        expected_money_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]

        total_money, money_list = main('./test-cases/casoG50.txt')

        self.assertEqual(total_money, expected_total_money)
        self.assertEqual(money_list, expected_money_list)

    def test_caseG50(self):
        expected_total_money = 104
        expected_money_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]

        total_money, money_list = main('./test-cases/casoG50.txt')

        self.assertEqual(total_money, expected_total_money)
        self.assertEqual(money_list, expected_money_list)

    def test_caseG100(self):
        expected_total_money = 104
        expected_money_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]

        total_money, money_list = main('./test-cases/casoG50.txt')

        self.assertEqual(total_money, expected_total_money)
        self.assertEqual(money_list, expected_money_list)

    def test_caseG200(self):
        expected_total_money = 104
        expected_money_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]

        total_money, money_list = main('./test-cases/casoG50.txt')

        self.assertEqual(total_money, expected_total_money)
        self.assertEqual(money_list, expected_money_list)


    def test_caseG750(self):
        expected_total_money = 104
        expected_money_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]

        total_money, money_list = main('./test-cases/casoG50.txt')

        self.assertEqual(total_money, expected_total_money)
        self.assertEqual(money_list, expected_money_list)

    def test_caseG1000(self):
        expected_total_money = 104
        expected_money_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]

        total_money, money_list = main('./test-cases/casoG50.txt')

        self.assertEqual(total_money, expected_total_money)
        self.assertEqual(money_list, expected_money_list)

    def test_caseG1500(self):
        expected_total_money = 104
        expected_money_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]

        total_money, money_list = main('./test-cases/casoG50.txt')

        self.assertEqual(total_money, expected_total_money)
        self.assertEqual(money_list, expected_money_list)

    def test_caseG2000(self):
        expected_total_money = 104
        expected_money_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]]

        total_money, money_list = main('./test-cases/casoG50.txt')

        self.assertEqual(total_money, expected_total_money)
        self.assertEqual(money_list, expected_money_list)
if __name__ == '__main__':
    unittest.main()