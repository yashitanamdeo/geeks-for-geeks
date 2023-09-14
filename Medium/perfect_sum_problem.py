# Problem Statement: https://practice.geeksforgeeks.org/problems/perfect-sum-problem5633/1

#User function Template for python3
class Solution:
	def perfectSum(self, arr, n, sum):
        mod=10**9+7
        dp=[[0]*(sum+1) for _ in range(n+1)]
        dp[0][0]=1
        for i in range(1,n+1):
            for j in range(sum+1):
                if arr[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=(dp[i-1][j]+dp[i-1][j-arr[i-1]])%mod
        return dp[n][sum]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,sum = input().split()
		n,sum = int(n),int(sum)
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.perfectSum(arr,n,sum)
		print(ans)

# } Driver Code Ends