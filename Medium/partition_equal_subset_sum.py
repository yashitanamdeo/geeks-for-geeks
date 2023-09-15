# Problem Statement: https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1

# User function Template for Python3

class Solution:

    def dfs(self,ind, n,target,arr,dp):
        if ind>=n:
            if target==0:
                return True
            return False
        if dp[ind][target]!=-1:
            return dp[ind][target]
        not_pick=self.dfs(ind+1,n,target, arr, dp)
        pick=False
        if target>=arr[ind]:
            
            pick=self.dfs(ind+1, n, target-arr[ind], arr, dp)
        dp[ind][target]=pick or not_pick
        return dp[ind][target]
    def equalPartition(self, N, arr):
        # code here
        if sum(arr)%2!= 0:
            return False
        target=sum(arr)//2
        dp=[[-1 for i in range(target+1)] for i in range((N))]
        return self.dfs(0, N, target, arr, dp)


#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends