# Problem Statement: https://practice.geeksforgeeks.org/problems/optimal-binary-search-tree2214/1

#User function Template for python3

class Solution:
    def optimalSearchTree(self, keys, freq, n):
        # code here
        dp = [[0 for i in range(n)] for j in range(n)]
        for g in range(n):
            for i,j in zip(range(n-g),range(g,n)):
                #print(i,j)
                if g == 0:
                    dp[i][j] = freq[i]
                if g == 1:
                    dp[i][j] = min(2*freq[i] + freq[j], 2*freq[j] + freq[i])
                else:
                    mini = 99999999999999
                    sumi = 0
                    for x in range(i,j+1):
                        sumi+=freq[x]
                    for k in range(i,j+1):
                        left = 0 if k == i else dp[i][k-1]
                        right = 0 if k == j else dp[k+1][j]
                        if left + right + sumi < mini:
                            mini = left + right + sumi
                    dp[i][j] = mini
                        
        #print(dp)
        return dp[0][n-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        n = int(input())
        keys = input().split()
        for itr in range(n):
            keys[itr] = int(keys[itr])
        freq = input().split()
        for itr in range(n):
            freq[itr] = int(freq[itr])
        ob = Solution()
        print(ob.optimalSearchTree(keys, freq, n))
# } Driver Code Ends