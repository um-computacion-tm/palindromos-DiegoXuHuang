import unittest
from palindrome import palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome_simple_true(self):
        result = palindrome('neuquen')
        self.assertEqual(result,True)

if __name__=='__main__':
    unittest.main()