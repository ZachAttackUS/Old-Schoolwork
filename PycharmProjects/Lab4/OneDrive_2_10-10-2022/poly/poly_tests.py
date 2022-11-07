import unittest
import poly

class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_poly_add2(self):
      poly1 = [1.4, 3.3, 5.6]
      poly2 = [2.1, 1.2, 2.9]
      poly3 = poly.poly_add2(poly1,poly2)
      self.assertListAlmostEqual(poly3, [3.5,4.5,8.5])


      poly1 = [3.2, 3.6, 1.9]
      poly2 = [2.6, 2.2, 8.5]
      poly3 = poly.poly_add2(poly1,poly2)
      self.assertListAlmostEqual(poly3, [5.8,5.8,10.4])

   def test_polymulti2(self):
      l1 = [2,4,1]
      l2 = [4,2,2]
      l3 = poly.poly_multi2(l1,l2)
      self.assertListAlmostEqual(l3,[8,20,16,10,2])

      l4 = [1, 1, 1]
      l5 = [1, 1, 1]
      l6 = poly.poly_multi2(l4, l5)
      self.assertListAlmostEqual(l6, [1, 2, 3, 2, 1])



   # Add tests here

if __name__ == '__main__':
   unittest.main()
