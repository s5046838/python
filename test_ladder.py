import unittest # module for testing purposes
import word_ladder as wordladder # imports word_ladder.py files as wordladder

class testWord(unittest.TestCase):  #creates a unittest class to initiate unit testing of functions


    def test_file(self,file):
        result = wordladder.file("dictionary.txt").read()
        self.assertTrue(len(result) != 0)

    def test_no_file(self):
        result = wordladder.file('dictionary.txt').read()
        self.assertFalse(len(result) == 0)

     def test_build(self):
         result = wordladder.build('empty.txt').read()
     def test_find(self):
         result = wordladder.find('empty.txt').read()


        def test_same(self, x, y):
            self.assertIn(wordladder.same(x, y))

    def test_wordRemove(self,path,word):
        self.assertIn(wordladder.wordRemove(path,word))

    unittest.main(exit=False) # runs the tests