# Problem Statement: https://www.geeksforgeeks.org/problems/maximum-profit4657/1

class Solution:
    def maxProfit(self, prices, k):
        # code here
        n=len(prices)
        dp=[[0] * n for _ in range(k+1)]
        if n<=1 or k ==0:
            return 0
        for i in range(1,k+1):
            dif=-prices[0]
            for j in range(1,n):
                dp[i][j]=max(dp[i][j-1],prices[j]+dif)
                dif=max(dif,dp[i-1][j]-prices[j])
        return dp[k][n-1]


#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends