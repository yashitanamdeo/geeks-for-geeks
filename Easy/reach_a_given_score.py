# Problem Statement: https://www.geeksforgeeks.org/problems/reach-a-given-score-1587115621/1

#User function Template for python3

class Solution:
    def count(self, n: int) -> int:
        #your code here
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(3,n+1):
            dp[i]=dp[i]+dp[i-3]
        for i in range(5,n+1):
            dp[i]=dp[i]+dp[i-5]
        for i in range(10,n+1):
            dp[i]=dp[i]+dp[i-10]
        return dp[-1]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ob = Solution()
        print(ob.count(n))
        
# } Driver Code Ends