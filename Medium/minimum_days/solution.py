# Problem Statement: https://practice.geeksforgeeks.org/problems/f4d22b1f9d62e8bee0ff84e9fa51dc66eb5005ec/1

from typing import List


class Solution:
    def getMinimumDays(self, N: int, S: str, P: List[int]) -> int:
        ans = 0
        S = list(S)
        i = 0
        while i < N-1:
            if P[i]+1 != N and S[P[i]] == S[P[i]+1] or (P[i] != 0 and S[P[i]] == S[P[i]-1]):
                S[P[i]] = '?'
                ans = i+1
            i += 1
        return ans


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

        S = (input())

        P = IntArray().Input(N)

        obj = Solution()
        res = obj.getMinimumDays(N, S, P)

        print(res)


# } Driver Code Ends
