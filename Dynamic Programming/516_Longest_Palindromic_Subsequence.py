# Problem: 516. Longest Palindromic Subsequence
# ------------------------------------------------
"""Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting 
some or no elements without changing the order of the remaining elements.
"""

class Solution:
    def longestPalindromeSubseq(self, s):
        self.memo = {}
        return self.helper(0, len(s) - 1, s)
    
    def helper(self, i, j, s):
        if i > j:
            return 0
        
        if i == j:
            return 1
        
        if (i, j) in self.memo:
            return self.memo[(i, j)]
        
        if s[i] == s[j]:
            self.memo[(i, j)] = 2 + self.helper(i + 1, j - 1, s)
        else:
            self.memo[(i, j)] = max(self.helper(i + 1, j, s), self.helper(i, j - 1, s))
        
        return self.memo[(i, j)]