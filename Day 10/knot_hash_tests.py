import unittest
from knot_hash import knot_hash

class KnotHashTests(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(knot_hash(""), "a2582a3a0e66e6e86e3812dcb672a272")

    def test_2(self):
        self.assertEqual(knot_hash("AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd")

    def test_3(self):
        self.assertEqual(knot_hash("1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d")

    def test_4(self):
        self.assertEqual(knot_hash("1,2,4"), "63960835bcdc130f0b66d7ff4f6a5a8e")



if __name__ == '__main__':
    unittest.main()
