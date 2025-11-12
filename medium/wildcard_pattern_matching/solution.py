# Problem Statement: https://www.geeksforgeeks.org/problems/wildcard-pattern-matching/1

class Solution:
    def wildCard(self, string: str, pattern: str) -> bool:
        n, m = len(string), len(pattern)
        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True

        for i in range(1, m+1):
            dp[i][0] = pattern[i-1] == '*' and dp[i-1][0]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if pattern[i-1] in ('?', string[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[i-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[m][n]