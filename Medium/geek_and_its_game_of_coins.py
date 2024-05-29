# Problem Statement: https://www.geeksforgeeks.org/problems/geek-and-its-game-of-coins4043/1


class Solution:
    def findWinner(self, n,x,y):
        dp=[0]*(n+1)
        for i in range(n):
            if dp[i]==0:
                dp[i+1]=1
                if i+x<=n:
                    dp[i+x]=1
                if i+y<=n:
                    dp[i+y]=1
        return dp[n]
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        obj = Solution()
        res = obj.findWinner(n, x, y)

        print(res)

# } Driver Code Ends