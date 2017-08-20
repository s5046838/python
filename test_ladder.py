import unittest # module for testing purposes
import word_ladder as wordladder # imports word_ladder.py files as wordladder

class testWord(unittest.TestCase):  #creates a unittest class to initiate unit testing of functions


    def test_file(self,file): # Tests whether the dictionary.txt file works
        result = wordladder.file("dictionary.txt").read()
        self.assertTrue(len(result) != 0)

    def test_no_file(self): # Tests whether the dictionary.txt file does not work
        result = wordladder.file('dictionary.txt').read()
        self.assertFalse(len(result) == 0)

    def test_build(self): # Tests whether the wrong file is being read
         result = wordladder.build('empty.txt').read()
         self.assertFalse(len(result) != 0)

    def test_same(self): # Tests the inputs for the word ladder if they work
        result = zip(1, 'one')
        self.assertTrue(result != 0)

    def test_same(self): # Tests the inputs for the word ladder if they don't
        result = zip(1, 'one')
        self.assertTrue(result == 0)


    def test_wordRemove(self, path, word): # Tests if the removed word is in the word path
        result = (path == word)
        self.assertTrue(result)

    def test_wordRemove(self, path, word):  # Tests if the removed word isn't in the word path
        result = (path != word)
        self.assertFalse(result)

    def test_wordRemove(self, path, word):  # Tests if the user starting word is equal to the word user wants removed
        result = (path != word[0])
        self.assertTrue(result)

    def test_userinput(self): #Checks if the user's input is not none
        result = input("")
        self.assertIsNotNone(result, '')

    unittest.main(exit=False) # runs the tests