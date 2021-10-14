import unittest
from cans import Cola
from customer import Customer
from coins import Quarter, Dime, Nickel, Penny
from soda_machine import SodaMachine

class TestSodaMachine(unittest.TestCase):
    def setUP(self):
        self.my_soda_machine = SodaMachine()

    def test_fill_register(self):
        """Test that its register list has a len of 88 """
        self.assertEqual(len(self.my_soda_machine.register), 88)
        print(len(self.my_soda_machine.register))    

    def test_fill_inventory(self):    
        """test that its inventory list has a len of 30"""
        self.assertEqual(len(self.my_soda_machine.inventory), 30)    