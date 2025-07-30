# Problem Statement: https://practice.geeksforgeeks.org/problems/number-of-enclaves/1

# User function Template for python3

from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.ans = 0

    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        n, m = len(grid), len(grid[0])
        visited = [[0] * m for _ in range(n)]
        q = deque()

        def isValid(
            i, j): return 0 <= i < n and 0 <= j < m and visited[i][j] == 0 and grid[i][j] == 1

        def bfs(q):
            while q:
                x, y = q.popleft()
                self.ans -= 1
                for i, j in [x+1, y], [x-1, y], [x, y+1], [x, y-1]:
                    if isValid(i, j):
                        q.append((i, j))
                        visited[i][j] = 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.ans += 1
                    if i == 0 or i == n-1 or j == 0 or j == m-1:
                        q.append([i, j])
                        visited[i][j] = 1

        bfs(q)
        return self.ans


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
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends
