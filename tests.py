import unittest
from prime_numbers import generate_prime

class TestPrime(unittest.TestCase):
    # Testing if the prime numbers work

    def test_accepts_numbers_only(self):
    # Give a parameter of int type

        self.assertEqual(generate_prime('str'), 'Pass numbers only')

    def test_accepts_positive_numbers(self):
    # Function to work with Positive integers

        self.assertEqual(generate_prime(10), [2, 3, 5, 7])
    
    def test_rejects_negative_values(self):
    # Function to reject negative intergers

        self.assertEqual(generate_prime(-10), "Provide a positive number")

    def test_returns_list(self):
    # To return a list

        self.assertIsInstance(generate_prime(10), list)

    def test_rejects_list_arguments(self):
    # To reject a list

        self.assertEqual(generate_prime([1, 2, 3]), 'Pass numbers only')
    
    def test_does_not_return_an_empty_list(self):
    # Function to return a list of prime numbers depending on the argument provided

        self.assertNotEqual(generate_prime(-10), [])