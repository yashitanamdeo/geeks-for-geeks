# Problem Statement: https://www.geeksforgeeks.org/problems/minimum-cost-to-make-two-strings-identical1107/1

#User function Template for python3
class Solution:
    def findMinCost(self, x, y, costX, costY):
		n, m = len(x), len(y)
        dp = [[0]*(m+1) for _ in range(n+1)]
            
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = 1+dp[i][j] if x[i] == y[j] else max(dp[i+1][j], dp[i][j+1])
        
        return costX*(n-dp[-1][-1])+costY*(m-dp[-1][-1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        X, Y, costX, costY = input().split()
        costX = int(costX)
        costY = int(costY)
        ob = Solution()
        ans = ob.findMinCost(X, Y, costX, costY)
        print(ans)

# } Driver Code Ends