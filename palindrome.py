import unittest

def palindrome(word):
    # rev_string = string[::-1]
    # text = ' '.string()
    # return text

    # word = word.lower().replace('','')
    if len(word)<= 1:
        return True
    if word[0] == word[-1]:
        return palindrome(word[1:-1])
    else:
        return False


    



# class TestPalindrome(unittest.TestCase):
#     def test_palindrome_simple_true(self):
#         result = palindrome('neuquen')
#         self.assertEqual(result,True)



if __name__=='__main__':
    unittest.main()
