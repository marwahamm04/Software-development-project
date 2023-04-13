import unittest
from final import coin_Calc 

class coin_CalcTest(unittest.TestCase):

    def test_if_it_there_is_out_come_(self):
        
        result = coin_Calc(7,0,0,0,0) 
        
        self.assertEqual(result, (0, 0, 1, 2))

    def test_if_quarters_work_(self):
        
        result = coin_Calc(56,0,0,0,0) 
        
        self.assertEqual(result, (2, 0, 0, 6))

    def test_if_it_negitive_gives_out_come_(self):
        
        result = coin_Calc(-8,0,0,0,0) 
        
        self.assertEqual(result, (0, 0, 0, 0))
    
    def test_if_negitive_gives_coins_outcome_(self):
        
        result = coin_Calc(-8,0,0,0,0) 
        
        self.assertNotEqual(result, (0, 5, 2, 0))
        
    def test_if_pennies_work_(self):
        
        result = coin_Calc(1,0,0,0,0) 
        
        self.assertEqual(result, (0, 0, 0, 1))

    

if __name__ == '__main__':
   unittest.main()
