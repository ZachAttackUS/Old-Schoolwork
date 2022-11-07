import unittest
import map
import point

class TestCases(unittest.TestCase):
   def test_square_all(self):
      list = [0,1,2,3,4]
      self.assertListEqual(map.square_all(list), [0,1,4,9,16])

   def test_square_all2(self):
      list = [1,4,7,2,9]
      self.assertListEqual(map.square_all(list), [1,16,49,4,81])

   def test_add_n_all1(self):
      list = [1,3,5,7,9]
      n = 4
      self.assertListEqual(map.add_n_all(list,n), [5,7,9,11,13])

   def test_add_n_add2(self):
      list = [7,2,4,9,1]
      n = 3
      self.assertListEqual(map.add_n_all(list,n), [10,5,7,12,4])

   def test_distance_all1(self):
      list = [point.Point(7,24), point.Point(3,4)]
      list_final = [25,5]
      self.assertListEqual(map.distance_all(list),list_final)

   def test_distance_all(self):
      list = [point.Point(6,8), point.Point(5,12),point.Point(9,12)]
      self.assertListEqual(map.distance_all(list), [10,13,15])










# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

