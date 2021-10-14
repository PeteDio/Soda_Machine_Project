import unittest
from cans import Cola
from customer import Customer
from coins import Quarter, Dime, Nickel, Penny
from soda_machine import SodaMachine

class TestSodaMachine(unittest.TestCase):
    def setUP(self):
        self.my_soda_machine = SodaMachine()