import unittest
from waterCubic import waterCubic

class TestWaterCubic(unittest.TestCase):
    """Test cases with different input data."""
    
    def test_data(self):
        obj = waterCubic([0,0,0,-1,-1,-1,-2,-3])
        a = obj.calculateWaterCubic()
        self.assertEqual(a, 8)

        obj = waterCubic([-1,2,-1,-2,1,4,-1,2])
        b = obj.calculateWaterCubic()
        self.assertEqual(b, 12)
    
    def test_data2(self):
        obj = waterCubic([1,2])
        c = obj.calculateWaterCubic()
        self.assertFalse(c, 1)

if __name__ == '__main__':
    unittest.main()