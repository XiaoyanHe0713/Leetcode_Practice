# Problem 221: Maximal Square
# ------------------------------------------------
"""Given an m x n binary matrix filled with 0's and 1's, find the largest square 
containing only 1's and return its area.
"""
class Solution:
    def maximalSquare(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_side = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side ** 2