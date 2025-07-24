# Problem Statement: https://www.geeksforgeeks.org/problems/find-pair-given-difference1559/1


from typing import List

class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        arr.sort()

        lo = 0
        for hi in range(1, n):
            while lo<hi-1 and arr[hi] - arr[lo] > x:
                lo += 1
            if arr[hi] - arr[lo] == x:
                return 1
            hi += 1
            
        return -1


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.findPair(n, x, arr)

        print(res)

# } Driver Code Ends