import unittest
from day9 import total_score

class StreamScoreCounterTests(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(total_score('{}'), (1, 0))

    def test_2(self):
        self.assertEqual(total_score('{{{}}}'), (6, 0))

    def test_3(self):
        self.assertEqual(total_score('{{},{}}'), (5, 0))

    def test_4(self):
        self.assertEqual(total_score('{{{},{},{{}}}}'), (16, 0))

    def test_5(self):
        self.assertEqual(total_score('{<a>,<a>,<a>,<a>}'), (1, 4))    

    def test_6(self):
        self.assertEqual(total_score('{{<ab>},{<ab>},{<ab>},{<ab>}}'), (9, 8))  

    def test_7(self):
        self.assertEqual(total_score('{{<!!>},{<!!>},{<!!>},{<!!>}}'), (9, 0))  

    def test_8(self):
        self.assertEqual(total_score('{{<a!>},{<a!>},{<a!>},{<ab>}}'), (3, 17))  



if __name__ == '__main__':
    unittest.main()
