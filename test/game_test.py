#!/usr/bin/env python3
import unittest
from unittest.case import TestCase
def new_game():
    return None
class game_test(unittest.TestCase):
   
    def test_game_is_blank(self):
        #given
        test_subject = new_game()
        #when
        #then
         #for item in test_subject:
        self.assertIsNone(test_subject)

    def test_game_is_9_by_9(self):
        #given
        test_subject = new_game()
        #when
        #then
         #for item in test_subject:
        self.assertEqual(len(test_subject), 3)

#return array of lens 3

if __name__ == "__main__":
    unittest.main()