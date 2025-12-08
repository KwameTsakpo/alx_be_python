import math
import unittest

class TestCase(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(sqr(8),2)
        
    def test_raise_error(self):
        with self.assertRaises(ValueError):
            sqr(-3)

def sqr(number):
    return math.sqrt(number)
    
if __name__ == '__main__':
    unittest.main()