import unittest
import data


class test_cases(unittest.TestCase):
    def test_Point(self):
        p1 = data.Point(5,6,7)
        self.assertEqual(p1.x, 5)
        self.assertEqual(p1.y, 6)
        self.assertEqual(p1.z, 7)

        p2 = data.Point(1,1,1)
        self.assertEqual(p2.x, 1)
        self.assertEqual(p2.y, 1)
        self.assertEqual(p2.z, 1)

        p3 = data.Point(7,2,3)
        self.assertEqual(p3.x, 7)
        self.assertEqual(p3.y, 2)
        self.assertEqual(p3.z, 3)

    def test_Vector(self):
        v1 = data.Vector(1,2,3)
        self.assertEqual(v1.x, 1)
        self.assertEqual(v1.y, 2)
        self.assertEqual(v1.z, 3)

        v2 = data.Vector(10,2,3)
        self.assertEqual(v2.x, 10)
        self.assertEqual(v2.y, 2)
        self.assertEqual(v2.z, 3)

        v3 = data.Vector(3,6,5)
        self.assertEqual(v3.x, 3)
        self.assertEqual(v3.y, 6)
        self.assertEqual(v3.z, 5)

    def test_Ray(self):
        test_point1 = data.Point(2,2,2)
        test_vector1 = data.Vector(4,4,4)
        test_ray1 = data.Ray(test_point1, test_vector1)
        self.assertEqual(test_ray1.pt, test_point1)
        self.assertEqual(test_ray1.dir, test_vector1)

        test_point2 = data.Point(1, 4, 4)
        test_vector2 = data.Vector(9, 3, 7)
        test_ray2 = data.Ray(test_point2, test_vector2)
        self.assertEqual(test_ray2.pt, test_point2)
        self.assertEqual(test_ray2.dir, test_vector2)

    def test_Sphere(self):
        test_center1 = data.Point(1,1,1)
        r = 2.2
        test_sphere = data.Sphere(test_center1, r)
        self.assertEqual(test_sphere.center, test_center1)
        self.assertEqual(test_sphere.radius, r)

        test_center2 = data.Point(4, 2, 4)
        r2 = 6.7
        test_sphere2 = data.Sphere(test_center2, r2)
        self.assertEqual(test_sphere2.center, test_center2)
        self.assertEqual(test_sphere2.radius, r2)












if __name__ == "__main__":
    unittest.main()