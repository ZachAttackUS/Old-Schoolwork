import unittest
import data
import vector_math
import collisions
from collisions import *

class test_cases(unittest.TestCase):
    def test_Point(self):
        p1 = data.Point(5, 6, 7)
        self.assertEqual(p1.x, 5)
        self.assertEqual(p1.y, 6)
        self.assertEqual(p1.z, 7)

        p2 = data.Point(1, 1, 1)
        self.assertEqual(p2.x, 1)
        self.assertEqual(p2.y, 1)
        self.assertEqual(p2.z, 1)

        p3 = data.Point(7, 2, 3)
        self.assertEqual(p3.x, 7)
        self.assertEqual(p3.y, 2)
        self.assertEqual(p3.z, 3)

    def test_Vector(self):
        v1 = data.Vector(1, 2, 3)
        self.assertEqual(v1.x, 1)
        self.assertEqual(v1.y, 2)
        self.assertEqual(v1.z, 3)

        v2 = data.Vector(10, 2, 3)
        self.assertEqual(v2.x, 10)
        self.assertEqual(v2.y, 2)
        self.assertEqual(v2.z, 3)

        v3 = data.Vector(3, 6, 5)
        self.assertEqual(v3.x, 3)
        self.assertEqual(v3.y, 6)
        self.assertEqual(v3.z, 5)

    def test_Ray(self):
        test_point1 = data.Point(2, 2, 2)
        test_vector1 = data.Vector(4, 4, 4)
        test_ray1 = data.Ray(test_point1, test_vector1)
        self.assertEqual(test_ray1.pt, test_point1)
        self.assertEqual(test_ray1.dir, test_vector1)

        test_point2 = data.Point(1, 4, 4)
        test_vector2 = data.Vector(9, 3, 7)
        test_ray2 = data.Ray(test_point2, test_vector2)
        self.assertEqual(test_ray2.pt, test_point2)
        self.assertEqual(test_ray2.dir, test_vector2)

    def test_Sphere(self):
        test_center1 = data.Point(1, 1, 1)
        r = 2.2
        test_sphere = data.Sphere(test_center1, r)
        self.assertEqual(test_sphere.center, test_center1)
        self.assertEqual(test_sphere.radius, r)

        test_center2 = data.Point(4, 2, 4)
        r2 = 6.7
        test_sphere2 = data.Sphere(test_center2, r2)
        self.assertEqual(test_sphere2.center, test_center2)
        self.assertEqual(test_sphere2.radius, r2)

    def test_scale(self):
        test_vector = data.Vector(1, 2, 3)
        test_vector_final = data.Vector(1.5, 3, 4.5)
        self.assertEqual(vector_math.scale_vector(test_vector, 1.5), test_vector_final)

        test_vector = data.Vector(5, 6, 7)
        test_vector_final = data.Vector(10, 12, 14)
        self.assertEqual(vector_math.scale_vector(test_vector, 2), test_vector_final)

    def test_length_vector(self):
        test_vector = data.Vector(1, 1, 1)
        self.assertEqual(vector_math.length_vector((test_vector)), False)

        test_vector = data.Vector(3, 4, 5)
        self.assertEqual(vector_math.length_vector((test_vector)), True)

    ##test normalize vector
    def test_normalize_vector(self):
        test_vector = data.Vector(3, 2, 6)
        self.assertEqual(vector_math.normalize_vector(test_vector), data.Vector(-3, -2, -6))

        test_vector = data.Vector(3, 2, 6)
        self.assertEqual(vector_math.normalize_vector(test_vector), data.Vector(-3, -2, -6))

    def test_difference_point(self):
        point1 = data.Point(3, 3, 3)
        point2 = data.Point(2, 2, 2)
        self.assertEqual(vector_math.difference_point(point1, point2), data.Vector(1, 1, 1))

        point1 = data.Point(7, 2, 9)
        point2 = data.Point(3, 1, 5)
        self.assertEqual(vector_math.difference_point(point1, point2), data.Vector(4, 1, 4))

    def test_difference_vector(self):
        vector1 = data.Vector(4, 6, 2)
        vector2 = data.Vector(2, 1, 1)
        self.assertEqual(vector_math.difference_vector(vector1, vector2), data.Vector(2, 5, 1))

        vector1 = data.Vector(8, 2, 5)
        vector2 = data.Vector(7, 1, 3)
        self.assertEqual(vector_math.difference_vector(vector1, vector2), data.Vector(1, 1, 2))

    def test_translate_point(self):
        point1 = data.Point(9, 1, 3)
        vector1 = data.Vector(3, 4, 2)
        self.assertEqual(vector_math.translate_point(point1, vector1), data.Point(12, 5, 5))

        point1 = data.Point(4, 2, 7)
        vector1 = data.Vector(6, 2, 8)
        self.assertEqual(vector_math.translate_point(point1, vector1), data.Point(10, 4, 15))

    def test_vector_from_to(self):
        to_point = data.Point(5, 8, 2)
        from_point = data.Point(4, 3, 1)
        self.assertEqual(vector_math.vector_from_to(from_point, to_point), data.Vector(1, 5, 1))

        to_point = data.Point(5, 7, 1)
        from_point = data.Point(8, 2, 4)
        self.assertEqual(vector_math.vector_from_to(from_point, to_point), data.Vector(-3, 5, -3))

    def test_sphere_intersection_point1(self):
        self.assertEqual(sphere_intersection_point(data.Ray(data.Point(2, 0, 0), data.Vector(8, 0, 0)),
                                                       data.Sphere(data.Point(7, 0, 0), 4)), data.Point(3, 0, 0))

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

    def test_find_intersection_points(self):
        ray = data.Ray((data.Point(2.4, 1, 0)), (data.Vector(6, 2.5, 0)))
        sphere = data.Sphere(data.Point(12, 5, 0), 3)
        sphere2 = data.Sphere(data.Point(3, 12, 4), 2)
        input_list = [sphere, sphere2]
        final_list = [(sphere, data.Point(9.23076, 3.84615, 0))]
        self.assertListEqual(find_intersection_points(input_list, ray), final_list)

    def test_find_intersection_points2(self):
        ray = data.Ray((data.Point(2, 0, 0)), (data.Vector(8, 0, 0)))
        sphere = data.Sphere(data.Point(7, 0, 0), 4)
        sphere2 = data.Sphere(data.Point(3, 12, 4), 2)
        input_list = [sphere, sphere2]
        final_list = [(sphere, data.Point(3, 0, 0))]
        self.assertListEqual(find_intersection_points(input_list, ray), final_list)


    def test_sphere_normal_at_point(self):
        sphere1 = data.Sphere(data.Point(1,1,1), 4)
        point1 = data.Point(0,0,0)
        self.assertEqual(collisions.sphere_normal_at_point(sphere1, point1), data.Vector(1,1,1))

    def test_sphere_normal_at_point1(self):
        sphere1 = data.Sphere(data.Point(2,2,2), 6)
        point1 = data.Point(1,1,1)
        self.assertEqual(collisions.sphere_normal_at_point(sphere1, point1), data.Vector(1,1,1))




if __name__ == "__main__":
    unittest.main()