import unittest
import vehicle

v1 = vehicle.vehicle(4,70,4,True)
class vehicleTests(unittest.TestCase):
   def test_vehicle1(self):
       self.assertEqual(v1.wheels, 4)
       self.assertEqual(v1.fuel, 70)
       self.assertEqual(v1.doors, 4)
       self.assertEqual(v1.roof, True)





# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

