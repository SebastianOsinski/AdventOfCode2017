import unittest
from day11 import count_steps

class KnotHashTests(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(count_steps("ne,ne,ne")[0], 3)

    def test_2(self):
        self.assertEqual(count_steps("ne,ne,sw,sw")[0], 0)

    def test_3(self):
        self.assertEqual(count_steps("ne,ne,s,s")[0], 2)

    def test_4(self):
        self.assertEqual(count_steps("se,sw,se,sw,sw")[0], 3)

if __name__ == '__main__':
    unittest.main()