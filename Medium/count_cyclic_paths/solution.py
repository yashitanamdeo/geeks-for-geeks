# Problem Statement: https://practice.geeksforgeeks.org/problems/aa0000a5f710ce8d41366b714341eef644ec7b82/1

#User function Template for python3

class Solution:
    def countPaths(self, N):
        if N == 1:
            return 0
        MOD = 10**9+7
        p2, p1 = 0, 1
        for i in range(2, N):
            p2, p1 = p1, (2*p1 + 3*p2) % MOD
        ans = (3*p1) % MOD
        return ans


#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.countPaths(N))

# } Driver Code Ends
