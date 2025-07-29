# Problem Statement: https://practice.geeksforgeeks.org/problems/95bb244da24edd6214086ff934886ccda6ed9da8/1

from typing import List
from math import inf
from collections import defaultdict


class Solution:
    def minTime(self, n: int, locations: List[int], types: List[int]) -> int:
        mn_loc, mx_loc = defaultdict(lambda: inf), defaultdict(lambda: -inf)
        for typ, loc in zip(types, locations):
            mn_loc[typ] = min(mn_loc[typ], loc)
            mx_loc[typ] = max(mx_loc[typ], loc)
        mn_prev, mx_prev = 0, 0
        dp = [(0, 0)]
        for typ in sorted(mn_loc):
            mn_cur, mx_cur = mn_loc[typ], mx_loc[typ]
            dp.append((min(dp[-1][0] + abs(mx_cur-mn_prev), dp[-1][1] + abs(mx_cur-mx_prev)) + mx_cur - mn_cur,
                       min(dp[-1][0] + abs(mn_cur-mn_prev), dp[-1][1] + abs(mn_cur-mx_prev)) + mx_cur - mn_cur))
            mn_prev, mx_prev = mn_cur, mx_cur

        return min(dp[-1][0] + abs(mn_cur), dp[-1][1] + abs(mx_cur))


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

        n = int(input())

        locations = IntArray().Input(n)

        types = IntArray().Input(n)

        obj = Solution()
        res = obj.minTime(n, locations, types)

        print(res)


# } Driver Code Ends
