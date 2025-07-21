# Problem Statement: https://practice.geeksforgeeks.org/problems/51b266505221b97522b1d2c86ddad1868a54831b/1

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
