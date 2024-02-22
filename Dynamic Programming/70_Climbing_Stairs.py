# Problem: 70. Climbing Stairs
# ------------------------------------------------
""" You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int, memo=dict({"1": 1, "2": 2})) -> int:
        if str(n) in memo:
            return memo[str(n)]
        else:
            memo[str(n)] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
            return memo[str(n)]