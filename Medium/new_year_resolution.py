# Problem Statement: https://www.geeksforgeeks.org/problems/good-by-2023/1


from typing import List


class Solution:
    def isPossible(self, N : int, coins : List[int]) -> bool:
        def helper(i,s):
            if s>0 and (s%20==0 or s%24==0 or s==2024):
                return True
            if i>=N:
                return False
            return helper(i+1,s+coins[i]) or helper(i+1,s)
        return helper(0,0)



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
        
        
        coins=IntArray().Input(N)
        
        obj = Solution()
        res = obj.isPossible(N, coins)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends
