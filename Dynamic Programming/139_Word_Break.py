# Problem 139. Word Break
# ------------------------------------------------
"""Given a string s and a dictionary of strings wordDict, 
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
"""

class Solution:
    def wordBreak(self, s, wordDict):
        self.memo = {}
        return self.canBreak(0, s, wordDict)
    
    def canBreak(self, i, s, wordDict):
        if i == len(s):
            return True
        
        if i in self.memo:
            return self.memo[i]
        
        for word in wordDict:
            if s[i:].startswith(word) and self.canBreak(i + len(word), s, wordDict):
                self.memo[i] = True
                return True
        
        self.memo[i] = False
        return False