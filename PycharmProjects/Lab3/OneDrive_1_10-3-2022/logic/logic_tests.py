import unittest
import logic

class TestCases(unittest.TestCase):
   def test_even(self):
      self.assertEqual(logic.is_even(4),True)
      self.assertEqual(logic.is_even(47),False)

   def test_interval(self):
      self.assertEqual(logic.in_an_interval(10), False)
      self.assertEqual(logic.in_an_interval(102),True)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

