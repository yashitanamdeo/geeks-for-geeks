# Problem Statement: https://practice.geeksforgeeks.org/problems/min-coin5549/1

#User function Template for python3

class Solution:
    def MinCoin(self, nums, amount):
        # Code here
        dp = [None for i in range(amount+1)]
        dp[0] = []
        for i in range(amount+1):
            if dp[i] is not None:
                for num in nums:
                    combination = [*dp[i], num]
                    if i + num <= amount:
                        if dp[i+num] is None or len(dp[i+num]) > len(combination):
                            dp[i+num] = combination
           
        if dp[amount] is None:
            return -1
        else:
            return len(dp[amount])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, amount = input().split()
		n = int(n)
		amount = int(amount)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.MinCoin(nums, amount)
		print(ans)
# } Driver Code Ends