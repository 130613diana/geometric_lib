import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5, 4), 20)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 7), 20)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 5), 10)

    def test_negative_sides_area(self):
        with self.assertRaises(ValueError):
            area(-1, 5)

    def test_negative_sides_perimeter(self):
        with self.assertRaises(ValueError):
            perimeter(4, -2)
