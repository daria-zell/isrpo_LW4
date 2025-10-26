import unittest


from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    # Тесты для площади
    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_positive_int(self):
        self.assertEqual(area(10, 12), 120)

    def test_area_positive_float(self):
        self.assertAlmostEqual(area(5.5, 7.2), 39.6)

    def test_area_square(self):
        self.assertEqual(area(5, 5), 25)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-10, 10)
        with self.assertRaises(ValueError):
            area(10, -10)
        with self.assertRaises(ValueError):
            area(-10, -10)
        with self.assertRaises(ValueError):
            area(0, -10)
        with self.assertRaises(ValueError):
            area(-10, 0)

    def test_area_string_side(self):
        with self.assertRaises(TypeError):
            area("10", 10)
        with self.assertRaises(TypeError):
            area(10, "10")
        with self.assertRaises(TypeError):
            area("10", "10")

    # Тесты для периметра
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(0, 10), 20)
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_positive_int(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(perimeter(5.5, 7.2), 25.4)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-10, 10)
        with self.assertRaises(ValueError):
            perimeter(10, -10)
        with self.assertRaises(ValueError):
            perimeter(-10, -10)
        with self.assertRaises(ValueError):
            perimeter(0, -10)
        with self.assertRaises(ValueError):
            perimeter(-10, 0)

    def test_perimeter_string_side(self):
        with self.assertRaises(TypeError):
            perimeter("10", 10)
        with self.assertRaises(TypeError):
            perimeter(10, "10")
        with self.assertRaises(TypeError):
            perimeter("10", "10")

if __name__ == '__main__':
    unittest.main()
