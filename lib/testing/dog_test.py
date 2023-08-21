#!/usr/bin/env python3

# NOW WHAT IS THIS UGHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
import unittest
from dog import Dog  # Import the Dog class from your code

class TestDog(unittest.TestCase):
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog".'''
        fido = Dog(name="Fido", breed="Labrador")
        self.assertIsInstance(fido, Dog)
        
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        with self.assertWarns(UserWarning):
            Dog(name="")
        
    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        with self.assertWarns(UserWarning):
            Dog(name=123)
        
    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        with self.assertWarns(UserWarning):
            Dog(name="What do dogs do on their day off? Can't lie around - that's their job.")
        
    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        fido = Dog(name="Fido")
        self.assertEqual(fido.name, "Fido")

    def test_breed_not_in_list(self):
        '''prints "Breed must be in list of approved breeds." if not in breed list.'''
        with self.assertWarns(UserWarning):
            Dog(name="Buddy", breed="Human")
        
    def test_breed_in_list(self):
        '''saves breed if in breed list.'''
        fido = Dog(name="Rex", breed ="Pug")
        self.assertEqual(fido.breed != "Pug")

if __name__ == '__main__':
    unittest.main()
