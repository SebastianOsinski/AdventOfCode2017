import unittest
from layer import Layer

class LayerScannerPositionTests(unittest.TestCase):
    
    def test_layer_with_range_2_time_0(self):
        self.assertEqual(Layer(2).scanner_position(0), 0)

    def test_layer_with_range_2_time_1(self):
        self.assertEqual(Layer(2).scanner_position(1), 1)

    def test_layer_with_range_2_time_2(self):
        self.assertEqual(Layer(2).scanner_position(2), 0)

    def test_layer_with_range_2_time_3(self):
        self.assertEqual(Layer(2).scanner_position(3), 1)

    def test_layer_with_range_2_time_4(self):
        self.assertEqual(Layer(2).scanner_position(4), 0)

    def test_layer_with_range_3_time_0(self):
        self.assertEqual(Layer(3).scanner_position(0), 0)

    def test_layer_with_range_3_time_1(self):
        self.assertEqual(Layer(3).scanner_position(1), 1)

    def test_layer_with_range_3_time_2(self):
        self.assertEqual(Layer(3).scanner_position(2), 2)

    def test_layer_with_range_3_time_3(self):
        self.assertEqual(Layer(3).scanner_position(3), 1)

    def test_layer_with_range_3_time_4(self):
        self.assertEqual(Layer(3).scanner_position(4), 0)    

    def test_layer_with_range_3_time_5(self):
        self.assertEqual(Layer(3).scanner_position(5), 1)    

    def test_layer_with_range_3_time_6(self):
        self.assertEqual(Layer(3).scanner_position(6), 2)    

    def test_layer_with_range_3_time_7(self):
        self.assertEqual(Layer(3).scanner_position(7), 1)    



if __name__ == '__main__':
    unittest.main()