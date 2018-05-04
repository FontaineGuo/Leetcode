## 020 Valid Parentheses
## Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
## determine if the input</br> string is valid.
## The brackets must close in the correct order, "()" and "()[]{}" are all valid 
## but "(]" and "([)]" are not.

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        test = list()
        for key, val in enumerate(s):
            if val in ['(', '{', '[']:
                test.append(val)
            elif len(test) == 0:
                return False
            else:
                c = test.pop()
                if {')':'(', '}':'{', ']':'['}[val] != c: #这是一个字典索引
                    return False
        if len(test) == 0:
            return True
        else:
            return False