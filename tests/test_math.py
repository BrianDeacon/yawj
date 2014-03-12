import unittest
import math

class TestMath(unittest.TestCase):

    def test_to_base_x(self):
        test_input = 0
        expected = '0'
        self.assertEqual(expected, math.to_base_x(test_input, 3))
        test_input = 1
        expected = '1'
        self.assertEqual(expected, math.to_base_x(test_input, 3))
        test_input = 2
        expected = '2'
        self.assertEqual(expected, math.to_base_x(test_input, 3))
        test_input = 3
        expected = '10'
        self.assertEqual(expected, math.to_base_x(test_input, 3))
        test_input = 4
        expected = '11'
        self.assertEqual(expected, math.to_base_x(test_input, 3))
        test_input = 5
        expected = '12'
        self.assertEqual(expected, math.to_base_x(test_input, 3))
        test_input = 6
        expected = '20'
        self.assertEqual(expected, math.to_base_x(test_input, 3))
        test_input = 7
        expected = '21'
        self.assertEqual(expected, math.to_base_x(test_input, 3))

    def test_to_base_x_padded(self):
        test_input = 7
        expected = '021'
        self.assertEqual(expected, math.to_base_x_padded(test_input, 3, 3))
        test_input = 7
        expected = '21'
        self.assertEqual(expected, math.to_base_x_padded(test_input, 3, 1))
        test_input = 7
        expected = '00021'
        self.assertEqual(expected, math.to_base_x_padded(test_input, 3, 5))

    def test_to_tic_tac_toe(self):
        min = 0
        max = (3^0) - 1
        for i in range(min, max):
            val = math.to_tic_tac_toe(i)
            self.assertEqual(9, len(val))
            num_val = math.to_base_x_padded(i, 3, 9)
            num_val = num_val.replace('0', ' ')
            num_val = num_val.replace('1', 'X')
            num_val = num_val.replace('2', 'O')
            self.assertEqual(num_val, val)
