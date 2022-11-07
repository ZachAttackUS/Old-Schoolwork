import unittest
import groups

class TestGroups(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_groups(self):
      list = [1,2,3,4,5,6]
      flist = [[1,2,3],[4,5,6]]
      self.assertListAlmostEqual(groups.groups_of_3(list), flist)

   def test_groups2(self):
      list = [3,5,3,2,4,7,8]
      flist = [[3,5,3],[2,4,7], [8]]
      self.assertListAlmostEqual(groups.groups_of_3(list), flist)



   # Add tests here

if __name__ == '__main__':
   unittest.main()
