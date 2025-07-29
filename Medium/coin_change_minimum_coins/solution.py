# Problem Statement: https://www.geeksforgeeks.org/problems/number-of-coins1824/1

class Solution:
	def minCoins(self, coins, sum):
        n=len(coins)
        dp=[float("inf")]*(sum+1)
        dp[0]=0
        for i in range(1,sum+1):
            for coin in coins:
                if i>=coin:
                    dp[i]=min(dp[i],1+dp[i-coin])
        return dp[sum] if dp[sum]!=float("inf") else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends