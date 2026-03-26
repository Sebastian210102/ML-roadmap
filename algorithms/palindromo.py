'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
 and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        s = "".join(filter(str.isalnum, s))

        left, rigth = 0 , len(s) -1

        while left < rigth:
            if s[left] != s[rigth]:
                return False
            left += 1
            rigth -= 1

        return True 
        