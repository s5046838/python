import unittest # module for testing purposes
import word_ladder as wordladder # imports word_ladder.py files as wordladder

class testWord(unittest.TestCase):  #creates a unittest class to initiate unit testing of functions

    # tests if the same function zips the two tuples together
    def test_same(self, x, y):
        self.assertIn(wordladder.same(x, y))

    # tests if the file is empty
    def test_file(self, file):
        result = wordladder.file('dictionary.txt').read()
        self.assertTrue(len(result) != 0)

    # test if there is no file
    def test_no_file(self):
        result = wordladder.file('empty.txt').read()
        self.assertTrue(len(result) == 0)

    # def test_build(self):
    #     result = wordladder.build('empty.txt').read()
    # def test_find(self):
    #     result = wordladder.find('empty.txt').read()

unittest.main() # runs the tests