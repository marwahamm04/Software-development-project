import unittest
from final import coin_Calc 

class coin_CalcTest(unittest.TestCase):

    def test_if_it_is_positive_number(self):
        
        result = coin_Calc(7,0,0,0,0) 
        
        self.assertEqual(result, (0, 0, 1, 2))

if __name__ == '__main__':
   unittest.main()
