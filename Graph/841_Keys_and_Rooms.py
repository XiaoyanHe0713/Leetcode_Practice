# Problem 841. Keys and Rooms
# ------------------------------------------------
"""There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
"""
class Solution:
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        visited = [0] * n
        self.dfs(rooms, visited, 0)
        return all(visited)
    
    def dfs(self, rooms, visited, i):
        visited[i] = 1
        for j in rooms[i]:
            if not visited[j]:
                self.dfs(rooms, visited, j)
            else:
                continue