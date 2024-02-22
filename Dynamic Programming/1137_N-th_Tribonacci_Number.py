# Problem: 1137. N-th Tribonacci Number
# ------------------------------------------------
"""The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
class Solution:
    def tribonacci(self, n: int, memo = dict ({"0": 0, "1": 1, "2": 1})):
        if str(n) in memo:
            return memo[str(n)]
        else:
            memo[str(n)] = self.tribonacci(n-1, memo) + self.tribonacci(n-2, memo) + self.tribonacci(n-3, memo)
            return memo[str(n)]