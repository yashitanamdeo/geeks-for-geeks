# Problem Statement: https://practice.geeksforgeeks.org/problems/9dacc32ad062be6e2ba8f6c41aad0b2b2376397d/1

#User function Template for python3

class Solution:
    def minCost(self, costs) -> int:
        import numpy as np
        N, K = len(costs), len(costs[0])
        if N<=0 or K<=0 or (K==1 and N>=2): return -1
        dp, tmp = costs[0].copy(), [0]*K
        for i in range(1, N):
            min1 = np.argmin(dp)
            min2 = min( (v,i) for i, v in enumerate(dp) if i!=min1 )[1]
            for j in range(K):
                tmp[j] = costs[i][j] + (dp[min1] if min1 != j else dp[min2])
            dp, tmp = tmp, dp
        return min(dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List


class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n, m = map(int, input().split())
        
        
        costs=IntMatrix().Input(n, m)
        
        obj = Solution()
        res = obj.minCost(costs)
        
        print(res)
# } Driver Code Ends