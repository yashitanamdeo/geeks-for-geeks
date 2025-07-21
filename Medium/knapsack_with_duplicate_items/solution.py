# Problem Statement: https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1

#User function Template for python3

class Solution:
    def knapSack(self, N, W, val, wt):
        dp=[None]*(W+1)
        for i in range(N+1):
            for j in range(W+1):
                if i==0:
                    dp[j]=0
                else:
                    dp[j]=max((val[i-1]+dp[j-wt[i-1]]) if j-wt[i-1]>=0 else 0, dp[j])
        return dp[W]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, W = [int(x) for x in input().split()]
        val = input().split()
        for itr in range(N):
            val[itr] = int(val[itr])
        wt = input().split()
        for it in range(N):
            wt[it] = int(wt[it])
        
        ob = Solution()
        print(ob.knapSack(N, W, val, wt))
# } Driver Code Ends