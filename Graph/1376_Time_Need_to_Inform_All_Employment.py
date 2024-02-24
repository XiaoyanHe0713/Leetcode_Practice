# Problem: 1376. Time Needed to Inform All Employees
# ------------------------------------------------
"""A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. 
Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, 
and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, 
all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.
"""
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:
        # Create a dictionary to store the subordinates of each employee
        subordinates = {}
        for i, m in enumerate(manager):
            if m not in subordinates:
                subordinates[m] = [i]
            else:
                subordinates[m].append(i)
        
        # Create a function to traverse the tree and calculate the time needed to inform all employees
        def dfs(employee):
            if employee not in subordinates:
                return 0
            return informTime[employee] + max(dfs(sub) for sub in subordinates[employee])
        
        return dfs(headID)