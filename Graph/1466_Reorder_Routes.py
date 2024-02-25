# Problem: 1466. Reorder Routes to Make All Paths Lead to the City Zero
# --------------------------------------------------------------
"""There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different 
cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because 
they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.
"""
from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections):
        # Create a dictionary to store the roads and their direction
        roads = defaultdict(list)
        for a, b in connections:
            roads[a].append((b, 1))
            roads[b].append((a, 0))
        
        # Create a set to store the visited nodes and a variable to store the number of edges to be changed
        visited = set()
        self.changes = 0
        
        # Traverse the graph using DFS
        def dfs(node):
            visited.add(node)
            for neighbor, direction in roads[node]:
                if neighbor not in visited:
                    self.changes += direction
                    dfs(neighbor)
        
        dfs(0)
        return self.changes