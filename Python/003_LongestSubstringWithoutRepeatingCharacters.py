## 003 Longest Substring Without Repeating Characters
## Given a string, find the length of 
## the longest substring without repeating 
## characters.

"""
Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring
""" 
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = -1
        maxLen = 0
        hashChar = {}
        
        for i in range(len(s)):
            if s[i] in hashChar and hashChar[s[i]] > start:
                start = hashChar[s[i]]
            hashChar[s[i]] = i
            maxLen = max(maxLen, i - start)
        
        return maxLen