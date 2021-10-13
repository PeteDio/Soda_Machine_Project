import unittest
from customer import Customer
from wallet import Wallet
from cans import Cola
from backpack import Backpack

class TestGetWalletCoin(unittest.TestCase):
    """Tests for Customer's get_wallet_coin method"""

    def setUp(self):
        self.customer = Customer()

    def test_can_return_quarter(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.value, .25)
    
    def test_can_return_penny(self):
        """Pass in 'Penny', method should return a Penny instance"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(returned_coin.value, .01)

    def test_can_return_dime(self):
        """Pass in 'Dime', method should return a Dime instance"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(returned_coin.value, .1)

    def test_can_return_nickel(self):
        """Pass in 'Nickel', method should return a Nickel instance"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.value, .05)
    
    def test_can_return_none(self):
        """Pass in random string, method should return none"""
        returned_coin = self.customer.get_wallet_coin('asdf')
        self.assertEqual(returned_coin, None)

class TestAddCoinsToWallet(unittest.TestCase):
    """Tests for Customer's add_coins_to_wallet method"""

    def setUp(self):
        self.customer = Customer()

    def test_add_coins_to_wallet_return_more(self):
        """Pass in a list of coins, should return the old length plus new coins"""
        self.wallet = Wallet()
        self.wallet.fill_wallet
        test_list_3 = ["Dime", "Nickel" , "Quarter"]
        before_coin_list = len(self.my_wallet.money)
        after_coin_list = len(self.add_coins_to_wallet(test_list_3))
        self.assertEqual(before_coin_list+3, after_coin_list)

    def test_add_coins_to_wallet_return_same(self):
        """Pass in a list of coins, should return the old length plus new coins"""
        test_list_3 = []
        before_coin_list = len(self.my_wallet.money)
        after_coin_list = len(self.add_coins_to_wallet(test_list_3))
        self.assertEqual(before_coin_list, after_coin_list)    



class TestAddCanToBackPack(unittest.TestCase):

    def setUP(self):
        self.customer = Customer()
        
    
    def test_add_can_to_backpack(self):
        """Pass in a can, should return the old length plus one"""
        self.backpack = Backpack()
        cola = Cola()
        before = len(self.backpack.purchased_cans)
        after = self.backpack.purchased_cans.append(cola)
        self.assertEqual(before+1, after)   
        

if __name__ == '__main__':
    unittest.main()