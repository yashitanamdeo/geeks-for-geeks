# Problem Statement: https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1

# User function Template for python3

import math


class Solution:
    def dfs(self, cache, dp, idx, length):
        if idx == length:
            return 0
        if cache[idx][length - 1] != -1:
            return cache[idx][length - 1]
        ans = math.inf
        for i in range(idx, length):
            if dp[idx][i] == True:
                ans = min(ans, 1 + self.dfs(cache, dp, i + 1, length))
        cache[idx][length - 1] = ans
        return ans

    def palindromicPartition(self, s):
        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]
        dp[length - 1][length - 1] = True
        for i in reversed(range(length - 1)):
            dp[i][i] = True
            for j in range(i + 1, length):
                dp[i][j] = (s[i] == s[j] and (
                    j == i + 1 or dp[i + 1][j - 1] == True))
        cache = [[-1 for _ in range(length)] for _ in range(length)]
        return self.dfs(cache, dp, 0, length) - 1


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        string = input()

        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends
