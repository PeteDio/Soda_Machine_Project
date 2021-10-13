import unittest
from customer import Customer

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

    def test_can_return_nickle(self):
        """Pass in 'Nickel', method should return a Nickel instance"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(returned_coin.value, .05)
    
    def test_can_return_none(self):
        """Pass in random string, method should return none"""
        returned_coin = self.customer.get_wallet_coin('asdf')
        self.assertEqual(returned_coin, None)

if __name__ == '__main__':
    unittest.main()


class TestAddCoinsToWallet(unittest.TestCase):
    """Tests for Customer's add_coins_to_wallet method"""
    def test_add_coins_to_wallet():
        pass

if __name__ == '__main__':
    unittest.main()