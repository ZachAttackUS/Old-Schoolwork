import unittest
import objects
import funcs_objects
from funcs_objects import *

class TestCases(unittest.TestCase):
   def test_cases_point(self):
      point1 = objects.Point(3,4)
      self.assertEqual(point1.x, 3)
      self.assertEqual(point1.y, 4)

   def test_cases_circle(self):
      test_Circle = objects.Circle(objects.Point(3,4), 5)
      self.assertEqual(test_Circle.center.x, 3)
      self.assertEqual(test_Circle.center.y, 4)
      self.assertEqual(test_Circle.r, 5)

   def test_distance(self):
      p1 = objects.Point(8,6)
      p2 = objects.Point(4,3)
      self.assertEqual(distance(p1,p2), 5)

      p3 = objects.Point(0,6)
      p4 = objects.Point(0,3)
      self.assertEqual(distance(p3,p4), 3)

   def test_circle_overlap(self):
      c1 = objects.Circle(objects.Point(5,2),4)
      c2 = objects.Circle(objects.Point(1,2),2)
      self.assertEqual(circle_overlap(c1,c2), True)

      c3 = objects.Circle(objects.Point(8,6), 2)
      c4 = objects.Circle(objects.Point(2,2), 2)
      self.assertEqual(circle_overlap(c3,c4), False)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

