# Problem Statement: https://practice.geeksforgeeks.org/problems/8d0e8785cef59cf4903b926ceb7100bcd16a9835/1

from typing import List
from collections import defaultdict


class Solution:
    def makePalindrome(self, n : int, arr : List[str]) -> bool:
        # code here
        l=list(arr)
        while len(l)>1:
            temp=l.pop()
            if temp[::-1] in l:
                l.remove(temp[::-1])
            else:
                return False
        if len(l)==0:
            return True
        if l[0]==l[0][::-1] :
            return True 
        else: 
            return False



#{ 
 # Driver Code Starts
class StringArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=input().strip().split()#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=StringArray().Input(n)
        
        obj = Solution()
        res = obj.makePalindrome(n, arr)
        
        result_val = "YES" if res else "NO"
        print(result_val)

# } Driver Code Ends