# Problem Statement: https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

from collections import deque
class Solution:
    def leaders(self, A, N):
        res=deque([A[N-1]])
        for i in range(N-2,-1,-1):
            if res[0]<=A[i]:
                res.appendleft(A[i])
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends