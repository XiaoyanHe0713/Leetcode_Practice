# Problem 5: Longest Palindromic Substring
# ------------------------------------------------
"""Given a string s, return the longest palindromic substring in s.
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        max_length = 1
        
        for i in range(len(s)):
            # Check for odd-length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_length = right - left + 1
                if curr_length > max_length:
                    max_length = curr_length
                    start = left
                left -= 1
                right += 1
            
            # Check for even-length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_length = right - left + 1
                if curr_length > max_length:
                    max_length = curr_length
                    start = left
                left -= 1
                right += 1
        
        return s[start:start+max_length]