# Problem Statement: https://practice.geeksforgeeks.org/problems/form-a-palindrome2544/1

#User function Template for python3

class Solution:
    def lcs(self,s,s1):
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(s) + 1)]
        for i in range(len(s) + 1):
            for j in range(len(s)+1):
                if(i == 0 or j == 0):
                    continue
                if(s[i-1] == s1[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]
        
    def findMinInsertions(self, s):
        return len(s) - self.lcs(s,s[::-1])
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        S = input().strip()
        ob=Solution()
        print(ob.findMinInsertions(S))
# } Driver Code Ends