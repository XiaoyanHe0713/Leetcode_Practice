# Problem: 802. Find Eventual Safe States
# ------------------------------------------------
"""There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
"""
class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        colored = [0] * n
        safe = []
        for i in range(n):
            if self.dfs(graph, colored, i):
                safe.append(i)
        return safe
    
    def dfs(self, graph, colored, i):
        if colored[i] > 0:
            return colored[i] == 2
        colored[i] = 1
        for j in graph[i]:
            if colored[j] == 2:
                continue
            if colored[j] == 1 or not self.dfs(graph, colored, j):
                return False
        colored[i] = 2
        return True
        