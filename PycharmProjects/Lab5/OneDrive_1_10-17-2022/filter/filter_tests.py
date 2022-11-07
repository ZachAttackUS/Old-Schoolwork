import unittest
import filter
import point

class TestCases(unittest.TestCase):
   def test_are_positive(self):
      list = [1,-3,-6,7]
      fin_list = [1,7]
      self.assertListEqual(filter.are_positive(list), fin_list)

      list2 = [-9, -2, 6, -4]
      fin_list2 = [6]
      self.assertListEqual(filter.are_positive(list2), fin_list2)

   def test_are_greater_than(self):
      list = [1,2,3,4,5,6,7]
      n = 3
      fin_list = [4,5,6,7]
      self.assertListEqual(filter.are_greater_than(list, n), fin_list)

      list2 = [43,23,10,3,8,9,24,54]
      n2 = 15
      fin_list2 = [43,23,24,54]
      self.assertListEqual(filter.are_greater_than(list2, n2), fin_list2)

   def test_are_in_first_quadrant(self):
      list = [point.Point(2,2), point.Point(-1,-1), point.Point(3,-2), point.Point(1,4)]
      fin_list = [point.Point(2,2),point.Point(1,4)]
      self.assertListEqual(filter.are_in_first_quadrant(list), fin_list)

   def test_are_in_first_quadrant(self):
      list = [point.Point(-3, 2), point.Point(5, 5), point.Point(3, -9), point.Point(8, 5)]
      fin_list = [point.Point(5, 5), point.Point(8, 5)]
      self.assertListEqual(filter.are_in_first_quadrant(list), fin_list)




# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

