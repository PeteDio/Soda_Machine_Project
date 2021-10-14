import unittest
from cans import Cola
from customer import Customer
from coins import Quarter, Dime, Nickel, Penny
from soda_machine import SodaMachine

class TestSodaMachine(unittest.TestCase):
    def setUp(self):
        self.my_soda_machine = SodaMachine()

    def test_fill_register(self):
        """Test that its register list has a len of 88 """
        self.assertEqual(len(self.my_soda_machine.register), 88)
        print(len(self.my_soda_machine.register))    

class TestFillInventory(unittest.TestCase):
    def setUp(self):
        self.my_soda_machine = SodaMachine()

    def test_fill_inventory(self):    
        """test that its inventory list has a len of 30"""
        self.assertEqual(len(self.my_soda_machine.inventory), 30)    


class TestGetCoinFromRegister(unittest.TestCase):
    def setUp(self):
            self.my_soda_machine = SodaMachine()

    def test_get_coin_from_register_Quarter(self):  
        """ Test if Quarter can be returned from register """
        returned_value = self.my_soda_machine.get_coin_from_register("Quarter")
        self.assertTrue(returned_value)

    def test_get_coin_from_register_dime(self):  
        """ Test if Dime can be returned from register """
        returned_value = self.my_soda_machine.get_coin_from_register("Dime")
        self.assertTrue(returned_value)

    def test_get_coin_from_register_penny(self):  
        """ Test if Penny can be returned from register """
        returned_value = self.my_soda_machine.get_coin_from_register("Penny")
        self.assertTrue(returned_value)

    def test_get_coin_from_register_nickel(self):  
        """ Test if Nickel can be returned from register """
        returned_value = self.my_soda_machine.get_coin_from_register("Nickel")
        self.assertTrue(returned_value)    

    def test_get_coin_from_register_rnd_str(self):
        """ Test if invalid coin return a value from register """
        returned_coin = self.my_soda_machine.get_coin_from_register("Asdf")
        self.assertIsNone(returned_coin, None)

class TestRegisterHasCoin(unittest.TestCase):
    def setUp(self):
        self.my_soda_machine = SodaMachine()

    def test_register_has_quarter(self):
        """Tests if register has quarters"""
        self.quarter = Quarter()
        returned_coin = self.my_soda_machine.register_has_coin(self.quarter.name)
        self.assertTrue(returned_coin)

    def test_register_has_dime(self):
        """Tests if register has dimes"""
        self.dime = Dime()
        returned_coin = self.my_soda_machine.register_has_coin(self.dime.name)
        self.assertTrue(returned_coin)

    def test_register_has_nickel(self):
        """Tests if register has nickels"""
        self.nickel = Nickel()
        returned_coin = self.my_soda_machine.register_has_coin(self.nickel.name)
        self.assertTrue(returned_coin)

    def test_register_has_penny(self):
        """Tests if register has pennies"""
        self.penny = Penny()
        returned_coin = self.my_soda_machine.register_has_coin(self.penny.name)
        self.assertTrue(returned_coin)

    def test_register_invalid_coin(self):
        """ Test if random string returns false """
        returned_coin = self.my_soda_machine.get_coin_from_register("Asdf")
        self.assertFalse(returned_coin)




if __name__ == '__main__':
    unittest.main()        