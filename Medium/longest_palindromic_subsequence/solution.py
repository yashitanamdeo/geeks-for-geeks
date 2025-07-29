# Problem Statement: https://practice.geeksforgeeks.org/problems/longest-palindromic-subsequence-1612327878/1

#User function Template for python3

class Solution:

    def longestPalinSubseq(self, S):
        R=S[::-1]
        n=len(S)
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if S[i-1]==R[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[n][n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends
