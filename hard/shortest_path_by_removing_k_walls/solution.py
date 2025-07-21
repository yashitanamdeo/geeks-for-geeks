# Problem Statement: https://practice.geeksforgeeks.org/problems/shortest-path-by-removing-k-walls/1

#User function Template for python3

from collections import deque


class Solution:
    def shotestPath(self, grid, n, m, k):
        # code here
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        q = deque([(0, 0, k, 0)])
        visited = set([(0, 0, k)])

        if (len(grid)-1) + (len(grid[0])-1) < k:
            return (len(grid)-1) + (len(grid[0])-1)

        while q:
            r, c, e, steps = q.popleft()
            for new_r, new_c in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if (new_r >= 0 and
                    new_r < len(grid) and
                    new_c >= 0 and
                        new_c < len(grid[0])):
                    if grid[new_r][new_c] == 1 and e > 0 and (new_r, new_c, e-1) not in visited:
                        visited.add((new_r, new_c, e-1))
                        q.append((new_r, new_c, e-1, steps+1))
                    if grid[new_r][new_c] == 0 and (new_r, new_c, e) not in visited:
                        if new_r == len(grid) - 1 and new_c == len(grid[0]) - 1:
                            return steps + 1
                        visited.add((new_r, new_c, e))
                        q.append((new_r, new_c, e, steps+1))
        return -1


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        mat = []
        for i in range(n):
            row = list(map(int, input().split()))
            mat.append(row)

        ob = Solution()
        print(ob.shotestPath(mat, n, m, k))
# } Driver Code Ends
