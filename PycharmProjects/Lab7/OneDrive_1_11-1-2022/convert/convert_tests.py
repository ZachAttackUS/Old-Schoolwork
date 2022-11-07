import unittest
import convert

class TestConvert(unittest.TestCase):
   def test_convert(self):
      self.assertEqual(convert.float_default('xyz'), 'xyz')

      self.assertEqual(convert.float_default('5'), 5)


if __name__ == '__main__':
   unittest.main()

