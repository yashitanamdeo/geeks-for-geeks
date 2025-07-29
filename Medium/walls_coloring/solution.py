# Problem Statement: https://www.geeksforgeeks.org/problems/walls-coloring--170646/0

# User function Template for python3

class Solution():
    def minCost(self, colors, N):

        p = b = y = 0
        for i in range(N):
            cp = min(b, y)+colors[i][0]
            cb = min(p, y)+colors[i][1]
            cy = min(p, b)+colors[i][2]
            p, b, y = cp, cb, cy
        return min(p, b, y)

class Solution2:
    def minCost(self, colors, N):
        a = [0] * N
        b = [0] * N
        c = [0] * N
        a[0] = colors[0][0]
        b[0] = colors[0][1]
        c[0] = colors[0][2]
        for i in range(1, N):
            a[i] = colors[i][0] + min(b[i-1], c[i-1])
            b[i] = colors[i][1] + min(a[i-1], c[i-1])
            c[i] = colors[i][2] + min(b[i-1], a[i-1])
        return min(a[N-1], b[N-1], c[N-1])


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        colors = []
        for i in range(n):
            tmp = [int(i) for i in input().split()]
            colors.append(tmp)
        print(Solution().minCost(colors, n))
# } Driver Code Ends
