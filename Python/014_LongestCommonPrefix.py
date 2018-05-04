## 014  Longest Common Prefix
## Write a function to find the longest 
## common prefix string amongst an array of strings.
"""
Examples:
["abc", "ab", "abd"]
output: "ab"
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        preFix = ""
        groupLen = len(strs)
        for index_1, word_1 in enumerate(strs[0]):
            for i in range(1, groupLen):
                if index_1 >= len(strs[i]) :
                    return preFix
                if strs[i][index_1] != word_1:
                    return preFix
            preFix += word_1
        return preFix