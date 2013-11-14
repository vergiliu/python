from unittest import TestCase
import unittest

import toy

class ToyTests(TestCase):
    def test_positive(self):
        self.assertEqual(toy.global_function(3), 4)

    def test_negative(self):
        self.assertEqual(toy.global_function(-3), -2)

    def test_large(self):
        self.assertEqual(toy.global_function(2**13), 2**13+1)

class TestExampleClass(TestCase):
    def test_times_two(self):
        example = toy.ExampleClass(5)
        self.assertEqual(example.times_two(), 10)

    def test_repr(self):
        example = toy.ExampleClass(7)
        self.assertEqual(repr(example), '<example param="7">')

if __name__ == "__main__":
    unittest.main()