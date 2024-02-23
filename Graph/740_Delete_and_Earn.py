# Problem: 740. Delete and Earn
# ------------------------------------------------
"""You are given an integer array nums. You want to maximize the number of points you get by performing the 
following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to 
nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some number of times.
"""
class Solution:
    def deleteAndEarn(self, nums) -> int:
        # Create a dictionary to store the frequency of each number in the input list
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Create a list to store the unique numbers in the input list
        nums = sorted(list(freq.keys()))
        
        # Create a list to store the maximum points that can be earned by deleting each number
        dp = [0] * (len(nums) + 1)
        
        # Traverse the list of unique numbers, and for each number, if it is not adjacent to the previous number, 
        # the maximum points that can be earned by deleting it is the product of its frequency and its value plus 
        # the maximum points that can be earned by deleting the previous number. If it is adjacent to the previous 
        # number, the maximum points that can be earned by deleting it is the maximum of the maximum points that can 
        # be earned by deleting it and the maximum points that can be earned by deleting the number before the 
        # previous number plus the product of its frequency and its value
        for i in range(1, len(nums) + 1):
            if nums[i - 1] - 1 != nums[i - 2]:
                dp[i] = max(dp[i - 1] + nums[i - 1] * freq[nums[i - 1]], dp[i - 2] + nums[i - 1] * freq[nums[i - 1]])
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1] * freq[nums[i - 1]])
        return dp[-1]