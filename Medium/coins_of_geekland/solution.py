# Problem Statement: https://practice.geeksforgeeks.org/problems/257a9e27fb3e58255622c8dcb06e0919cc1c6c11/1#

#User function Template for python3

class Solution:
    def Maximum_Sum(self, mat, N, K):
        # Your code goes here
        maximum_sum=0
        dp=[[0 for _ in range(n+1)]for _ in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                if (i==0 or j==0):
                    dp[i][j]=0
                else:
                    dp[i][j]=mat[i-1][j-1]+dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]
                if (i>=k and j>=k):
                    maximum_sum=max(dp[i][j]-(dp[i][j-k]+dp[i-k][j]-dp[i-k][j-k]),maximum_sum)
        return maximum_sum

#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        matrix=[]
        for _ in range(n):
            matrix.append( [ int(x) for x in input().strip().split() ] )
        k=int(input())
        obj = Solution()
        print(obj.Maximum_Sum(matrix,n,k))
# } Driver Code Ends