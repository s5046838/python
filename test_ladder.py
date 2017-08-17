from word_ladder import same, build, find # Imports the functions from the word_ladder python file
import unittest
import re



class testWord(unittest.TestCase):  #creates a unittest class to initiate unit testing of functions

    # tests if the self function zips the two tuples together
    def test_same(self, x, y):
      self.assertIn(same(x, y))

unittest.main()