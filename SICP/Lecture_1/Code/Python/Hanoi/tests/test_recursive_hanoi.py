import unittest

import recursive_hanoi

class TestRecursiveHanoi(unittest.TestCase):
    def test_gen_moving_seq(self):
        self.assertEqual([[1, 'F', 'T'], [2, 'F', 'S'], [1, 'T', 'S'],
                          [3, 'F', 'T'], [1, 'S', 'F'], [2, 'S', 'T'],
                          [1, 'F', 'T']],
                         recursive_hanoi.gen_moving_seq(3, 'F', 'T', 'S'))