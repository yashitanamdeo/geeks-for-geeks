from typing import List

class Solution:

    def maximum_profit(self, n : int, intervals : List[List[int]]) -> int:
        intervals.sort( key=lambda x: (x[1], x[0]) )
        M = intervals[-1][1]
        dp = [0]*(M+1)
        
        for i in range(n):
            s,e,p = intervals[i]
            if p+dp[s] > dp[e]:
                dp[e] = p+dp[s]
            if i < n-1:
                _,en,_ = intervals[i+1]
                for j in range(e+1, en+1):
                    dp[j] = dp[e]
                
        return dp[M]
