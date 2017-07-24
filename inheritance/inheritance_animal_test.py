import unittest
from inheritance_animal import *


class DogTest(unittest.TestCase):
    def setUp(self):
        self.dog = Dog('rover');

    def test_fetch(self):
        self.assertEqual("rover goes after the beach-ball", self.dog.fetch("beach-ball"))