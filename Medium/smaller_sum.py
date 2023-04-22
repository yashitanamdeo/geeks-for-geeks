# Problem Statement: https://practice.geeksforgeeks.org/problems/5877fde1c8e1029658845cd4bc94066ac1d4b09b/1

from typing import List


class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        # code here
        d={}
        x=arr.copy()
        x.sort()
        s=0
        ans=[]
        for i in range(n):
            if x[i] not in d:
                d[x[i]]=s
            s+=x[i]
        for i in arr:
            ans.append(d[i])
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
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.smallerSum(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends