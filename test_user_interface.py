import unittest
import user_interface 
from cans import Cola, OrangeSoda, RootBeer
from coins import Quarter, Dime, Nickel, Penny

class TestUserInterface(unittest.TestCase):
    
    def test_validate_main_menu(self):
        """Validating if passing 1, tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(1)
        self.assertEqual(returned_value, (True, 1))

    def test_validate_main_menu_two(self):
        """Validating if passing 2, tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(2)
        self.assertEqual(returned_value, (True, 2))

    def test_validate_main_menu_three(self):
        """Validating if passing 3, tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(3)
        self.assertEqual(returned_value, (True, 3))

    def test_validate_main_menu_four(self):
        """Validating if passing 4, tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(4)
        self.assertEqual(returned_value, (True, 4))    

    def test_validate_main_menu_b(self):
        """Validating if passing 5, fapple (False, None) will be returned"""
        returned_value = user_interface.validate_main_menu(5)
        self.assertEqual(returned_value, (False, None)) 

class TestTryParseInt(unittest.TestCase):

    def test_try_parse_int(self):
        """10 as a string goes in, needs to return int value 10"""
        returned_value = user_interface.try_parse_int('10')
        self.assertEqual(returned_value, 10)
        pass

    def test_try_parse_int_b(self):
        """'hello' goes in, needs to return 0"""
        returned_value = user_interface.try_parse_int('hello')
        self.assertEqual(returned_value, 0)

class TestGetUniqueCanNames(unittest.TestCase):

    def test_get_unique_can_names(self):
        """Instantiate 6 cans (two of each type) and append them to a list. Pass the list into this function, ensure the returned list only contains 3 names"""

        cola = Cola()
        cola_one = Cola()
        orange_soda = OrangeSoda()
        orange_soda_one = OrangeSoda()
        root_beer = RootBeer()
        root_beer_one = RootBeer()
        
        soda_list = []

        soda_list.append(cola)
        soda_list.append(cola_one)
        soda_list.append(orange_soda)
        soda_list.append(orange_soda_one)
        soda_list.append(root_beer)
        soda_list.append(root_beer_one)

        returned_value = user_interface.get_unique_can_names(soda_list)
        self.assertEqual(len(returned_value), 3)

    def test_get_unique_can_names_empty(self):
        """Pass in an empty list. Ensure an empty list is returned."""
        self.my_soda = []

        returned_value = user_interface.get_unique_can_names(self.my_soda)
        self.assertEqual(len(returned_value), 0)


class TestDisplayPaymentValue(unittest.TestCase):

    def test_display_payment_value(self):
        """Instantiate each of the 4 coin types and append them to a list. Pass the list into this function, ensure the returned values is .41"""
        quarter = Quarter()
        dime = Dime()
        nickel = Nickel()
        penny = Penny()

        wallet = []

        wallet.append(quarter)
        wallet.append(dime)
        wallet.append(nickel)
        wallet.append(penny)

        returned_value = user_interface.display_payment_value(wallet)
        self.assertEqual(returned_value, .41)

    def test_display_payment_value_b(self):
        """Pass in an empty list. Ensure the returned value is 0."""
        self.wallet = []

        returned_value = user_interface.display_payment_value(self.wallet)
        self.assertEqual(returned_value, 0)

class TestValidateCoinSelection(unittest.TestCase):
        
    def test_validate_coin_selection_a(self):
        """Pass in each int 1, ensure the appropriate tuple is returned."""
        returned_value = user_interface.validate_coin_selection(1)
        self.assertEqual(returned_value, (True, "Quarter"))

    def test_validate_coin_selection_b(self):
        """Pass in each int 2, ensure the appropriate tuple is returned."""
        returned_value = user_interface.validate_coin_selection(2)
        self.assertEqual(returned_value, (True, "Dime"))

    def test_validate_coin_selection_c(self):
        """Pass in each int 3, ensure the appropriate tuple is returned."""
        returned_value = user_interface.validate_coin_selection(3)
        self.assertEqual(returned_value, (True, "Nickel"))

    def test_validate_coin_selection_d(self):
        """Pass in each int 4, ensure the appropriate tuple is returned."""
        returned_value = user_interface.validate_coin_selection(4)
        self.assertEqual(returned_value, (True, "Penny"))

    def test_validate_coin_selection_e(self):
        """Pass in each int 5, ensure the appropriate tuple is returned."""
        returned_value = user_interface.validate_coin_selection(5)
        self.assertEqual(returned_value, (True, "Done"))
    
    def test_validate_coin_selection_f(self):
        """Pass in a different number, ensure (False, None) is returned."""
        returned_value = user_interface.validate_coin_selection(6)
        self.assertEqual(returned_value, (False, None))

if __name__ == "__main__":
    unittest.main()        