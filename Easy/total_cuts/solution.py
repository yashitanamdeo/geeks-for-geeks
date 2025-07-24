# Problem Statement: https://practice.geeksforgeeks.org/problems/cbd515a00f6537180d2e66f1ffe11093a128e560/1

from typing import List


class Solution:
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        # code here
        left=[A[0]]
        for i in range(1,N):
            left.append(max(A[i],left[-1]))
        right=[A[-1]]
        for i in range(N-2,-1,-1):
            right.append(min(A[i],right[-1]))
        right=right[::-1]
        ans=0
        for i in range(1,N):
            if left[i-1]+right[i]>=K:
                ans+=1
        return ans
        



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
        
        
        K = int(input())
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.totalCuts(N,K,A)
        
        print(res)
        

# } Driver Code Ends
