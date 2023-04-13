import unittest
from final import coin_Calc 

class coin_CalcTest(unittest.TestCase):

    def test_if_it_there_is_out_come_(self):
        
        result = coin_Calc(7,0,0,0,0) 
        
        self.assertEqual(result, (0, 0, 1, 2))

    def test_if_it_eight_gives_out_come_(self):
        
        result = coin_Calc(8,0,0,0,0) 
        
        self.assertEqual(result, (0, 0, 1, 3))

if __name__ == '__main__':
   unittest.main()
