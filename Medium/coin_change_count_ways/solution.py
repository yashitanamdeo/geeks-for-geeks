# Problem Statement: https://practice.geeksforgeeks.org/problems/coin-change2448/1

# User function Template for python3

import sys


class Solution:
    def count(self, coins, N, Sum):
        dp = [[0] * (Sum + 1) for _ in range(N + 1)]

        for i in range(N + 1):
            dp[i][0] = 1

        for i in range(1, N + 1):
            for j in range(1, Sum + 1):
                take = 0
                if coins[i - 1] <= j:
                    take = dp[i][j - coins[i - 1]]
                ntake = dp[i - 1][j]
                dp[i][j] = take + ntake

        return dp[N][Sum]


# {
 # Driver Code Starts
# Initial Template for Python 3
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        sum, N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins, N, sum))

# } Driver Code Ends
