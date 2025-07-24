# Problem Statement: https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1

#User function Template for python3

class Solution:

    def lcs(self,x,y,s1,s2):
        dp=[[0]*(y+1) for z in range(x+1)]
        for i in range(x):
            for j in range(y):
                if s1[i]==s2[j]:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends
