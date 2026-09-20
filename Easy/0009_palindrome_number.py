# Problem: Palindrome Number
# Difficulty: Easy

class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return True if x == x[::-1] else False