# Problem Statement: https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1

#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
        dp=[0]
        dp.extend(Arr)
        for i in range(2,n+1):
            for j in range(1,i):
                if Arr[i-1]>Arr[j-1]:
                    dp[i]=max(dp[i],dp[j]+Arr[i-1])
        return max(dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends