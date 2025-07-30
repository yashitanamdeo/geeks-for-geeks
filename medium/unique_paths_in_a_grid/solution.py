# Problem Statement: https://practice.geeksforgeeks.org/problems/96161dfced02d544fc70c71d09b7a616fe726085/1

#User function Template for python3

class Solution:
    def uniquePaths(self, n, m, grid):
        if grid[0][0] == 0 or grid[n-1][m-1] == 0:
            return 0
        vs = [0]*m
        vs[0] = 1
        for r in range(n):
            vs[0] = 0 if grid[r][0] == 0 else vs[0]
            for c in range(1, m):
                if grid[r][c]:
                    vs[c] += vs[c-1]
                else:
                    vs[c] = 0
        return vs[m-1] % (10**9+7)


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())

        grid = []
        for i in range(n):
            col = list(map(int, input().split()))
            grid.append(col)

        ob = Solution()
        print(ob.uniquePaths(n, m, grid))
# } Driver Code Ends
