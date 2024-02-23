# Problem: 198. House Robber
# ------------------------------------------------
"""You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you 
from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were 
broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution:
    def rob(self, nums):
        self.memo = {}
        return self.robFromI(0, nums)

    def robFromI(self, i, nums):
        if i >= len(nums):
            return 0
        
        if i in self.memo:
            return self.memo[i]
        
        # Recursive relation evaluation to get the optimal answer.
        self.memo[i] = max(self.robFromI(i + 1, nums), self.robFromI(i + 2, nums) + nums[i])
        return self.memo[i]