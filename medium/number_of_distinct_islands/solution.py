# Problem Statement: https://practice.geeksforgeeks.org/problems/number-of-distinct-islands/1

# User function Template for python3

import sys
from typing import List
import collections


class Solution:

    def bfs(self, i, j, grid, visited):
        n, m = len(grid), len(grid[0])
        queue = collections.deque()
        visited[i][j] = True
        queue.append([i, j])
        directions = [(1, 0, "R"), (-1, 0, "L"), (0, -1, "U"), (0, 1, "D")]
        curr = ""
        while len(queue) > 0:
            x, y = queue.popleft()
            for dx, dy, move in directions:
                nx = x+dx
                ny = y+dy
                if (0 <= nx < n) and (0 <= ny < m) and grid[nx][ny] == 1 and visited[nx][ny] == False:
                    curr += move
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                else:
                    curr += "E"
        return curr

    def countDistinctIslands(self, grid: List[List[int]]) -> int:
        # code here
        n, m = len(grid), len(grid[0])
        hashset = set()
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j] == False:
                    moves = self.bfs(i, j, grid, visited)
                    hashset.add(moves)
        return len(hashset)

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj = Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends
