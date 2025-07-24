# Problem Statement: https://practice.geeksforgeeks.org/problems/trace-path3840/1

# User function Template for python3

class Solution:
    def isPossible(self, n, m, s):
        minx, maxx, miny, maxy = 0, 0, 0, 0
        dx, dy = 0, 0
        for d in s:
            if d == 'L':
                dx -= 1
            if d == 'R':
                dx += 1
            if d == 'U':
                dy += 1
            if d == 'D':
                dy -= 1
            minx = min(minx, dx)
            maxx = max(maxx, dx)
            miny = min(miny, dy)
            maxy = max(maxy, dy)
        return int(maxx-minx < m and maxy-miny < n)


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        s = input()

        ob = Solution()
        print(ob.isPossible(n, m, s))
# } Driver Code Ends
