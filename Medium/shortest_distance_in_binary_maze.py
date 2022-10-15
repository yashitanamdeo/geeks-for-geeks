# Problem Statement: https://practice.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1

#User function Template for python3

from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque([])
        q.append((source, 0))
        grid[source[0]][source[1]] = 0

        while q:

            (r, c), count = q.popleft()

            if [r, c] == destination:
                return count

            for dr, dc in directions:
                row = r+dr
                col = c+dc

                if row not in range(rows) or col not in range(cols) or grid[row][col] == 0:
                    continue

                grid[row][col] = 0
                q.append(((row, col), count + 1))

        return -1


#{
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        source = [0] * 2
        source[0], source[1] = map(int, input().strip().split())
        destination = [0] * 2
        destination[0], destination[1] = map(int, input().strip().split())
        obj = Solution()
        print(obj.shortestPath(grid, source, destination))
# } Driver Code Ends
