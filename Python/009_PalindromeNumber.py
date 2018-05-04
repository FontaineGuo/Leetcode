## 009 Palindrome Number

## Determine whether an integer is 
## a palindrome. Do this without extra space.

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        temp = x
        y = 0
        while temp != 0 :
            y = (y*10) + (temp%10)
            temp = temp//10
            
        if y == x:
            return True
        else:
            return False