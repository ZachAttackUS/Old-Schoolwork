import unittest
import funcs


class TestCases(unittest.TestCase):
    def test_square(self):
        # Add code here.
        self.assertEqual(funcs.f(1), 9)

    def test_f(self):
        # Add code here.
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
