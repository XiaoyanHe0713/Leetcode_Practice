# Problem: 1129. Shortest Path with Alternating Colors
# ------------------------------------------------
"""You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.
"""
from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges, blueEdges):
        # Create a dictionary of lists to store the adjacent nodes for each node and the color of the edge
        adjacents = {i: [[], []] for i in range(n)}
        for i, j in redEdges:
            adjacents[i][0].append(j)
        for i, j in blueEdges:
            adjacents[i][1].append(j)
        
        # Create a queue to store the nodes to be visited and a list to store the visited nodes, where each element in
        # the list is a triplet (node, distance, color). The queue is initialized with the first two nodes and the
        # two colors
        queue = deque([(0, 0, 0), (0, 0, 1)])

        # Create a list to store the visited nodes and the color of the edge
        visited = [[0, 0] for _ in range(n)]
        visited[0] = [1, 1]
        result = [-1] * n
        
        # Traverse the graph using BFS
        while queue:
            node, distance, color = queue.popleft()

            # For each node, if it's the first time reaching it, the distance is recorded in result. Then, 
            # for each adjacent node reachable via an edge of the opposite color to the last one used, if 
            # that node has not been visited via an edge of this new color, it is marked as visited and added 
            # to the queue with an incremented distance and the new color
            if result[node] == -1:
                result[node] = distance
            for neighbor in adjacents[node][color]:
                if not visited[neighbor][color]:
                    visited[neighbor][color] = 1
                    queue.append((neighbor, distance + 1, 1 - color))
        return result