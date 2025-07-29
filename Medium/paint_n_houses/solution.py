# Problem Statement: https://practice.geeksforgeeks.org/problems/844b4fdcd988ac5461324d62d43f7892749a113c/1

#User function Template for python3

class Solution:
    def distinctColoring(self, N, r, g, b):
        d = [r[0], g[0], b[0]]
        for i in range(1, N):
            c = [1e12, 1e12, 1e12]
            c[0] = min(d[1]+r[i], d[2]+r[i])
            c[1] = min(d[2]+g[i], d[0]+g[i])
            c[2] = min(d[0]+b[i], d[1]+b[i])
            d = c
        return min(d)


#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        r = list(map(int, input().split()))
        g = list(map(int, input().split()))
        b = list(map(int, input().split()))

        ob = Solution()
        print(ob.distinctColoring(N, r, g, b))
# } Driver Code Ends
