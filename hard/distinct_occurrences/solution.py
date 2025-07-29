# Problem Statement: https://www.geeksforgeeks.org/problems/distinct-occurrences/1

# Your task is to complete this function
# Function should return Integer
class Solution:
    def sequenceCount(self,s, t):
        # Code here
        MOD = 10**9 + 7
        n, m = len(s), len(t)
        dp = [0] * (m + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] = (dp[j] + dp[j - 1]) % MOD
    
        return dp[m]


#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends