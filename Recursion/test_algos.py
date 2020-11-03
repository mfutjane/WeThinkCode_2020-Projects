import unittest
from super_algos import *

class MyTests(unittest.TestCase):

    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5, 6, 7]), 1)
        self.assertEqual(find_min([33, 2, -45, -4, 5, 0, -7]), -45)
        self.assertEqual(find_min(['a', 'b', 'c']), -1)
        self.assertEqual(find_min([4, 23, 'c']), -1)
        self.assertRaises(ValueError, find_min, {1, 2, 3})
        self.assertRaises(ValueError, find_min, (1, 2, 3))

    def test_sum_all(self):
        self.assertEqual(sum_all([1, 2, 3, 4, 5, 6, 7]), 28)
        self.assertEqual(sum_all([33, 2, -45, -4, 5, 0, -7]), -16)
        self.assertEqual(sum_all(['a', 'b', 'c']), -1)
        self.assertEqual(sum_all([4, 23, 'c']), -1)
        self.assertRaises(ValueError, sum_all, {1, 2, 3})
        self.assertRaises(ValueError, sum_all, ('a', 'b', 'c'))

    def test_find_possible_strings(self):
        self.assertEqual(find_possible_strings(['a', 'b', 'c'], 2), ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'])
        self.assertEqual(find_possible_strings(['a', 'b', 'c'], 1), ['a', 'b', 'c'])
        self.assertEqual(find_possible_strings(['a', 'b', 3], 3), [])
        self.assertEqual(find_possible_strings([4, (1,2), 'c'], 3), [])
        self.assertRaises(ValueError, find_possible_strings, {'a', 'b', 'c'}, 2)
        self.assertRaises(ValueError, find_possible_strings, (1, 2, 3), 2)