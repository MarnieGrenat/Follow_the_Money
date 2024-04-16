import unittest
from Script.Olympus.Atlas import Atlas


class AtlasTest(unittest.TestCase):
    def setUp(self):
        self.map = Atlas(".\AtlasUnitTest.txt")

    def test_load_map(self):
        _ = self.map._WALL
        h = self.map._HORIZONTAL_STREET
        v = self.map._VERTICAL_STREET
        c, x = self.map._CURVE
        E = self.map._DEAD_END
        expected_map = [
            [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,   E, _],
            [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,   v, _],
            [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,  '0',_],
            [h,h,h,h,h,h,h,h,h,h,h,h, c,_,_,_,_,_,_,_, '1',_],
            [_,_,_,_,_,_,_,_,_,_,_,_,'8',_,_,_,_,_,_,_,'2',_],
            [_,_,_,_,_,_,_,_,_,_,_,_, v,_,_,_,_,_,_,_, '3',_],
            [_,_,_,_,_,_,_,_,_,_,_,_, v,_,_,_,_,_,_,_, '4',_],
            [_,_,_,_,_,_,_,_,_,_,_,_, c,h,h,h,h,h,h,h, '5',c],
            [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,   v, v],
            [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,   v, v],
            [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,   v, v],
            [_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,   c, x]
        ]
        self.assertEqual(self.map.map, expected_map)

    def test_find_start(self):
        expected_start = 1
        self.assertEqual(self.map.start, expected_start)

    def test_set_as_VISITED(self):
        self.map.set_as_VISITED(2, 3)
        self.assertEqual(self.map.map[2][3, ' '], self.map._VISITED)

if __name__ == '__main__':
    unittest.main()