# Problem Statement: https://www.geeksforgeeks.org/problems/find-the-closest-number5513/1

import math
from typing import List


class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        low, high = 0, len(arr) - 1
        ans = -math.inf
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == k: return k
            if arr[mid] <= k:
                if ans == -math.inf or abs(ans - k) > abs(arr[mid] - k):
                    ans = arr[mid]
                low = mid + 1
            else:
                if ans == -math.inf or abs(ans - k) >= abs(arr[mid] - k):
                    ans = arr[mid]
                high = mid - 1
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
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findClosest(n, k, arr)
        
        print(res)
        

# } Driver Code Ends