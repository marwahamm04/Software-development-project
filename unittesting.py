import unittest
from final import coin_Calc

class coin_calcTest(unittest.TestCase):

    def test_if_nickels_work(self):

        result = coin_Calc(5, 0, 0, 0, 0)

        self.assertEqual(result, (0, 0, 1, 0))

    def test_if_dimes_work(self):

        result = coin_Calc(10, 0, 0, 0, 0)

        self.assertEqual(result, (0, 1, 0, 0))

    def test_if_nickels_not_equal(self):

        result = coin_Calc(5, 0, 0, 0, 0)

        self.assertNotEqual(result, (0, 0, 5, 0))

    def test_if_dimes_not_equal(self):

        result = coin_Calc(5, 0, 0, 0, 0)

        self.assertNotEqual(result, (0, 5, 0, 0))

    def test_if_pennies_not_equal(self):

        result = coin_Calc(20, 0, 0, 0, 0)

        self.assertNotEqual(result, (0, 0, 0, 15))


if __name__ == '__main__':
   unittest.main()
