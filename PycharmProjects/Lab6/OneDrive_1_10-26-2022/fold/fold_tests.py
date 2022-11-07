import unittest
import fold
import point

class TestCases(unittest.TestCase):
   def test_sum1(self):
      inputlist = [1,2,3,4,5]
      self.assertEqual(fold.sum_of_values(inputlist), 15)

      inputlist2 = [1,4,6,9,2]
      self.assertEqual(fold.sum_of_values(inputlist2), 22)

   def test_index_of_smallest(self):
      inputlist = [1,2,3,4,5]
      self.assertEqual(fold.index_of_smallest(inputlist), 0)

      inputlist2 = []
      self.assertEqual(fold.index_of_smallest(inputlist2), -1)


   def test_nearest_origin(self):
      inputlist = [point.Point(3,4),point.Point(5,5)]
      self.assertEqual(fold.nearest_origin(inputlist), 0)

      inputlist = []
      self.assertEqual(fold.nearest_origin(inputlist), -1)




# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

