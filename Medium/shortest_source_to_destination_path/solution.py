# Problem Statement: https://practice.geeksforgeeks.org/problems/shortest-source-to-destination-path3544/1

# User function Template for python3

import math


class Solution:

    def shortestDistance(self, rows, cols, grid, target_row, target_col):
        if grid[0][0] == 0 or grid[target_row][target_col] == 0:
            return -1
        path_length, queue, neighbors = 0, [[0, 0]], [
            [0, -1], [-1, 0], [1, 0], [0, 1]]

        while queue:
            next_queue = []
            for row, col in queue:
                if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                    continue
                if row == target_row and col == target_col:
                    return path_length
                grid[row][col] = 0
                next_queue.extend(
                    [[row, col - 1], [row - 1, col], [row + 1, col], [row, col + 1]])
            queue, path_length = next_queue, path_length + 1
        return -1


# {
 # Driver Code Starts

# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().strip().split())
        a = []
        for i in range(N):
            s = list(map(int, input().strip().split()))
            a.append(s)
        x, y = map(int, input().strip().split())
        ob = Solution()
        print(ob.shortestDistance(N, M, a, x, y))

# } Driver Code Ends
