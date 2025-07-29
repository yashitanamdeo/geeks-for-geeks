# Problem Statement: https://www.geeksforgeeks.org/problems/buy-and-sell-a-share-at-most-twice/1

from typing import List


class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        left, right = [0]*n, [0]*n
        
        minv = price[0]
        for i in range(1, n):
            minv = min(minv, price[i])
            left[i] = max(left[i-1], price[i]-minv)
            
        maxv = price[-1]
        for i in range(n-2, -1, -1):
            maxv = max(maxv, price[i])
            right[i] = max(right[i+1], maxv-price[i])
    
        return max([x+y for x, y in zip(left, right)])
        



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
        
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.maxProfit(n, price)
        
        print(res)
        

# } Driver Code Ends