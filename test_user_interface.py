import unittest
import user_interface
from cans import Cola, OrangeSoda, RootBeer
from coins import Quarter, Dime, Nickel
class TestUserInterface(unittest.TestCase):
    
    def test_validate_main_menu(self):
        """Validating if passing 1 tupple (True, number) will be returned"""
        returned_value = user_interface.validate_main_menu(1)
        self.assertEqual(returned_value, (True, 1))