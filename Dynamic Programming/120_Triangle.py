# Problem: 120. Triangle
# ------------------------------------------------
"""Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More 
formally, if you are on index i on the current row, you may move to either 
index i or index i + 1 on the next row.
"""
class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]