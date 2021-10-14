import unittest
from cans import Cola, OrangeSoda, RootBeer
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
        quarter = Quarter()
        returned_coin = self.my_soda_machine.register_has_coin(quarter.name)
        self.assertTrue(returned_coin)

    def test_register_has_dime(self):
        """Tests if register has dimes"""
        dime = Dime()
        returned_coin = self.my_soda_machine.register_has_coin(dime.name)
        self.assertTrue(returned_coin)

    def test_register_has_nickel(self):
        """Tests if register has nickels"""
        nickel = Nickel()
        returned_coin = self.my_soda_machine.register_has_coin(nickel.name)
        self.assertTrue(returned_coin)

    def test_register_has_penny(self):
        """Tests if register has pennies"""
        penny = Penny()
        returned_coin = self.my_soda_machine.register_has_coin(penny.name)
        self.assertTrue(returned_coin)

    def test_register_invalid_coin(self):
        """ Test if random string returns false """
        returned_coin = self.my_soda_machine.get_coin_from_register("Asdf")
        self.assertFalse(returned_coin)

class TestDetermineChangeValue(unittest.TestCase):
    def setUp(self):
        self.my_soda_machine = SodaMachine()

    def test_determine_change_value_a(self):
        """test if change returned total_price higher """
        changed_value = self.my_soda_machine.determine_change_value(1.00, .50)
        self.assertEqual(changed_value, 0.5)

    def test_determine_change_value_b(self):
        """test if change returned soda_price higher """
        changed_value = self.my_soda_machine.determine_change_value(1.00, 1.50)
        self.assertEqual(changed_value, -0.5)

    def test_determine_change_value_c(self):
        """test if change returned two equal values from register """
        changed_value = self.my_soda_machine.determine_change_value(1.00, 1.00)
        self.assertEqual(changed_value, 0)
        
class TestCalculateCoinValue(unittest.TestCase):
    def setUp(self):
        self.my_soda_machine = SodaMachine()

    def test_calculate_coin_value(self):
        """Passing through each type of coin and making sure the value is correct"""
        quarter = Quarter()
        nickel = Nickel()
        dime = Dime()
        penny = Penny()
        

        self.money_list = []
        self.money_list.append(quarter)
        self.money_list.append(nickel)
        self.money_list.append(dime)
        self.money_list.append(penny)

        

        self.assertEqual(self.my_soda_machine.calculate_coin_value(self.money_list), .41)

    def test_calculate_coin_value_with_zero(self):
        """passing through nothing should return 0"""
        self.money_list = []
        self.assertEqual(self.my_soda_machine.calculate_coin_value(self.money_list), 0)        


class TestGetInventorySoda(unittest.TestCase):
    def setUp(self):
        self.my_soda_machine = SodaMachine()

    def test_get_inventory_soda_a(self):
        """taking the name property and checking it against it's actual name"""
        cola = Cola()
        orange_soda = OrangeSoda()
        root_beer = RootBeer()
        self.soda_one = self.my_soda_machine.get_inventory_soda(cola.name)
        self.soda_two = self.my_soda_machine.get_inventory_soda(orange_soda.name)
        self.soda_three = self.my_soda_machine.get_inventory_soda(root_beer.name)
        self.assertEqual(self.soda_one.name, "Cola")
        self.assertEqual(self.soda_two.name, "Orange Soda")
        self.assertEqual(self.soda_three.name, "Root Beer")
        
    def test_get_inventory_soda_b(self):
        """Sending in a string and checking against other names should return None"""
        self.soda_one = self.my_soda_machine.get_inventory_soda('Mountain Deu')
        self.assertIsNone(self.soda_one)

class TestReturnInventory(unittest.TestCase):
    def setUp(self):
        self.my_soda_machine = SodaMachine()

    def test_return_inventory(self):
        """storing the length of the inventory adding a can then testing the stored length plus one againist the new length"""
        before_inventory = len(self.my_soda_machine.inventory)
        cola = Cola()
        len(self.my_soda_machine.return_inventory(cola))
        after_inventory = len(self.my_soda_machine.inventory)

        self.assertEqual(before_inventory + 1, after_inventory)  



if __name__ == '__main__':
    unittest.main()        