# Problem Statement: https://practice.geeksforgeeks.org/problems/111fb97b983399c0ee9f34b7bae18ac76bf6f07a/1

from typing import List


class Solution:
    def maxCoins(self, n, ranges):

        ranges.sort(key=lambda e: (e[1], e[0]))

        maxv, ends = [], []
        sofar, ans = 0, 0
        for start, end, v0 in ranges:
            lo, hi = 0, len(ends)
            while lo < hi:
                mi = lo+(hi-lo)//2
                if ends[mi] <= start:
                    lo = mi+1
                else:
                    hi = mi
            v = v0
            if 0 <= lo-1 < len(ends):
                v += maxv[lo-1]
            ans = max(ans, v)
            ends.append(end)
            sofar = max(sofar, v0)
            maxv.append(sofar)
        return ans


# {
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        ranges = IntMatrix().Input(n, 3)

        obj = Solution()
        res = obj.maxCoins(n, ranges)

        print(res)


# } Driver Code Ends
