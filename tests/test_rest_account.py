from __future__ import absolute_import
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, 1)
        self.assertEqual(2, 2)
        self.assertEqual(2, 2)


