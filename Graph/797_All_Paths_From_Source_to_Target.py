# Problem: 797. All Paths From Source to Target
# ------------------------------------------------
"""Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 
to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a 
directed edge from node i to node graph[i][j]).
"""
class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)

        # Define a backtracking function that traverses the graph backwards
        def backtrack(currNode, path):
            # If we reach the target node, no need to explore further.
            if currNode == n - 1:
                res.append(list(path))
                return
            # Explore the neighbors of the current node
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()

        res = []
        backtrack(0, [0])
        return res