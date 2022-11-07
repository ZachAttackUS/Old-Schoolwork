import unittest
import data
from collisions import *

class TestCases2(unittest.TestCase):
    def test_sphere_intersection_point1(self):
        self.assertEqual(sphere_intersection_point(data.Ray(data.Point(2, 0, 0), data.Vector(8, 0, 0)), data.Sphere(data.Point(7, 0, 0), 4)), data.Point(3, 0, 0))

    def test_sphere_intersection_point2(self):
        ray = data.Ray(data.Point(2.4, 1, 0), data.Vector(6, 2.5, 0))
        sphere = data.Sphere(data.Point(12, 5, 0), 3)
        intersection = sphere_intersection_point(ray, sphere)
        self.assertEqual(intersection, data.Point(9.23076, 3.84615, 0))

    def test_sphere_intersection_point3(self):
        ray = data.Ray(data.Point(0, 0, 0), data.Vector(3, 12, 4))
        sphere = data.Sphere(data.Point(3, 12, 4), 2)
        intersection = sphere_intersection_point(ray, sphere)
        self.assertEqual(intersection, data.Point(2.53846, 10.15384, 3.38461))


if __name__ == '__main__':
    unittest.main()
