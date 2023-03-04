# Problem Statement: https://practice.geeksforgeeks.org/problems/a3493283697b7b69573a840f371a55ccd9332bb0/1

from typing import List


class Solution:
    def bestNode(self, N: int, A: List[int], P: List[int]) -> int:
        def _solve(ix):
            if cs[ix]:
                for c in cs[ix]:
                    _solve(c)
                dp[ix] = max(A[ix] - A[i] + cmax[i] for i in cs[ix])
                cmax[ix] = max(dp[i] for i in cs[ix])
            else:
                dp[ix] = A[ix]
                cmax[ix] = 0

        cs = [[] for _ in range(N)]
        dp, cmax = [0] * N, [0] * N
        for i in range(1, N):
            cs[P[i]-1].append(i)
        _solve(0)
        return max(dp)


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

        N = int(input())

        A = IntArray().Input(N)

        P = IntArray().Input(N)

        obj = Solution()
        res = obj.bestNode(N, A, P)

        print(res)


# } Driver Code Ends
