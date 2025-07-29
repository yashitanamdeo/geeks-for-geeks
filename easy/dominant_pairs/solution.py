# Problem Statement: https://practice.geeksforgeeks.org/problems/2a1c11024ceae36363fc405e07f2fa3e2f896ef0/1

from typing import List


class Solution:
    def dominantPairs(self, n: int, arr: List[int]) -> int:
        # code here
        arr[:n//2] = sorted(arr[:n//2])
        arr[n//2:] = sorted(arr[n//2:])
        i = 0
        j = n//2
        count = 0

        while i < n//2 and j < n:
            if arr[i] >= 5*arr[j]:
                count += n//2-i
                j += 1
            else:
                i += 1

        return count


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

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.dominantPairs(n, arr)

        print(res)


# } Driver Code Ends
