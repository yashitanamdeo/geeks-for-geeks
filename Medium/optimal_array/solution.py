# Problem Statement: https://practice.geeksforgeeks.org/problems/d4aeef538e6dd3280dda5f8ed7964727fdc7075f/1

from typing import List


class Solution:
    def optimalArray(self, n: int, a: List[int]) -> List[int]:
        # code here
        for i in range(n - 1, 0, -1):
            a[i] -= a[i >> 1]
        a[0] = 0
        for i in range(1, n):
            a[i] += a[i - 1]
        return a


#{
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        a = IntArray().Input(n)

        obj = Solution()
        res = obj.optimalArray(n, a)

        IntArray().Print(res)


# } Driver Code Ends
