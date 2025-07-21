# Problem Statement: https://practice.geeksforgeeks.org/problems/subset-sum-problem2014/1

# User function Template for Python3

class Solution1:

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

class Solution2:
    
    def f(self,arr,size,index,s,current,dp):
        if current ==(s/2):
            return 0
        if index >size -1 :
            return float('inf')
        ans=float('inf')
        #take cndn  
        if dp [index][current]!=-1:
            return dp[index][current]
        if (current +arr[index]) < s:
            ans = self.f(arr,size,index+1,s,current+arr[index],dp)
        if ans==0:
            return 0
        #not take cndn 
        ans=self.f(arr,size,index+1,s,current,dp)
        dp[index][current]= ans
        return dp[index][current]
    
    def equalPartition(self, arr):
        size =len (arr)
        s=0
        for i in range (size):
            s+=arr[i]
        dp = [[-1]*(s+1) for i in range (size)]    
        ans =self.f(arr,size,0,s,0,dp)
        if (ans==0):
            return True 
        return False
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