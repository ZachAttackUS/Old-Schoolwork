import unittest
import conditional

class TestCases(unittest.TestCase):
   def test_max_101(self):
      self.assertEqual(conditional.max_101(5,4), 5)
      self.assertEqual(conditional.max_101(3,1),3)

   def test_max_of_three(self):
      self.assertEqual(conditional.max_of_three(2,3,4), 4)
      self.assertEqual(conditional.max_of_three(40, 10, 90,), 90)

   def test_rental_fee(self):
      self.assertEqual(conditional.rental_late_fee(8), 5)
      self.assertEqual(conditional.rental_late_fee(15), 7)




# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

