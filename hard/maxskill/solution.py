# Problem Statement: https://practice.geeksforgeeks.org/problems/burst-balloons/1


from typing import List
import sys

class Solution:
    def maxCoins(self, n : int, nums : List[int]) -> int:
        # code here
        nums.insert(0,1)
        nums.append(1)
        dp=[[0 for i in range(n+2)] for j in range(n+2)]
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i>j:
                    continue
                maxi=-sys.maxsize-1
                for ind in range(i,j+1):
                    cost=nums[i-1]*nums[ind]*nums[j+1]+dp[i][ind-1]+dp[ind+1][j]
                    maxi=max(maxi,cost)
                    dp[i][j]=maxi
        return dp[1][n]



#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxCoins(N, arr)
        
        print(res)
        

# } Driver Code Ends