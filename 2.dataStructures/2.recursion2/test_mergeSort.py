import unittest
from mergeSort import mergeSort

class TestMergeSort(unittest.TestCase):
    
    def test_mergeSort(self):
        # Test case 1: Empty list
        self.assertEqual(mergeSort([]), [])
        
        # Test case 2: List with one element
        self.assertEqual(mergeSort([5]), [5])
        
        # Test case 3: List with multiple elements
        self.assertEqual(mergeSort([5, 3, 8, 6, 2, 7]), [2, 3, 5, 6, 7, 8])
        
        # Test case 4: List with duplicate elements
        self.assertEqual(mergeSort([5, 3, 8, 6, 2, 7, 3]), [2, 3, 3, 5, 6, 7, 8])
        
        # Test case 5: List with negative numbers
        self.assertEqual(mergeSort([-5, 3, -8, 6, 2, -7, 0]), [-8, -7, -5, 0, 2, 3, 6])
        
if __name__ == '__main__':
    unittest.main()
