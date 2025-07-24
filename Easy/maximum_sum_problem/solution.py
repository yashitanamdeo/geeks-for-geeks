# Problem Statement: https://www.geeksforgeeks.org/problems/maximum-sum-problem2211/1

#User function Template for python3

class Solution:
    def maxSum(self, n): 
        dp = [-1] * (n+1)
        
        def helper(i):
            if i == 0:  # terminating condition
                return 0
            
            if dp[i] != -1:
                return dp[i]
                
            dp[i] = max(i, helper(i//2) + helper(i//3 )+ helper(i//4))
            return dp[i]
        
        return helper(n)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends