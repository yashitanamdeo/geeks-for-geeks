# Problem Statement: https://practice.geeksforgeeks.org/problems/number-of-paths0926/1

# User function Template for python3

class Solution:
    def numberOfPaths(self, m, n):
        path = 1
        Mod = 10**9 + 7
        for i in range(m - 1):
            path = (path*(i+n)) % Mod
            temp = pow(i+1, Mod-2, Mod)
            path = (path*temp) % Mod
        return path


# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)


# } Driver Code Ends
