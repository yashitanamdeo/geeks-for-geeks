# Problem Statement: https://practice.geeksforgeeks.org/problems/1ccf56f107bcb24242469ea45c02f852165a2184/1

from typing import List


class Solution:
    def minimumInteger(self, N : int, A : List[int]) -> int:
        # code here
        S=0
        y=0
        pr=1
        sum=0
        ans=0
        for x in A:
            if(ans<x):
                ans=x
            
            sum=sum+x
            
        
        for y in A:
            pr=y*N
            if(pr==sum):
                return y
            if(pr>=sum):
                if(ans>y):
                    ans=y
                
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
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.minimumInteger(N, A)
        
        print(res)
        

# } Driver Code Ends