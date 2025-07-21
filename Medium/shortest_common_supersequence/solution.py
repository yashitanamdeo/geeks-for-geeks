# Problem Statement: https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1

#User function Template for python3

class Solution:
    def shortestCommonSupersequence(self, str1, str2, len_str1, len_str2):
        dp = [[-1 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]

        for i in range(len_str1 + 1):
            for j in range(len_str2 + 1):
                if not i or not j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + dp[i - 1][j - 1] if str1[i - 1] == str2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])

        return len_str1 + len_str2 - dp[len_str1][len_str2]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends