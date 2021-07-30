import unittest
from sec import bank

class Testsec(unittest.TestCase):
    
    def test_details(self):
        print("test_detail")
        customer = bank("joshua", "1227365349")
        self.assertEqual(customer.details, "Account name:joshua, Account number:1227365349")

if __name__ == "__main__":
    unittest.main()
