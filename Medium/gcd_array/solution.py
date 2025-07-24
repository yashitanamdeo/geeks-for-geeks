# Problem Statement: https://practice.geeksforgeeks.org/problems/2b70d42632a4e207569c6d2d777383e4603d6fe1/1


from typing import List

import math


class Solution:

    def solve(self, N: int, K: int, arr: List[int]) -> int:

        # code here
        a = sum(arr)
        d = []
        m = int(a ** 0.5)
        for i in range(1, m+1):
            if a % i == 0:
                d.append(i)
                if i != (a // i):
                    d.append(a // i)
        d.sort(reverse=True)
        for i in range(1, N):
            arr[i] += arr[i-1]
        out = 1
        for x in d:
            cnt = 0
            for y in arr:
                if (y % x == 0):
                    cnt += 1
            if cnt >= K:
                out = x
                break
        return out


# {
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

        N = int(input())

        K = int(input())

        arr = IntArray().Input(N)

        obj = Solution()
        res = obj.solve(N, K, arr)

        print(res)


# } Driver Code Ends
