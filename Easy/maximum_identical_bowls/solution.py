# Problem Statement: https://practice.geeksforgeeks.org/problems/5bfe93cc7f5a214bc6342709c78bc3dceba0f1c1/1


from typing import List
class Solution:
    def getMaximum(self, N : int, arr : List[int]) -> int:
        x=sum(arr)
        for i in range(N,1,-1):
            if x%i==0:
                return i
        return 1       
        



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
        res = obj.getMaximum(N, arr)
        
        print(res)
        

# } Driver Code Ends