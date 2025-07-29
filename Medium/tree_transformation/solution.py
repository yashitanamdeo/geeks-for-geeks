# Problem Statement: https://practice.geeksforgeeks.org/problems/fbcd1787378ed396a8f24b47872cbc0ad2624f1d/1

from typing import List


class Solution:
    def solve(self, N: int, p: List[int]) -> int:
        nodes = [0]*N

        for i in range(1, N):
            nodes[p[i]] += 1
            nodes[i] += 1

        leaf_cnt = sum(1 for n in nodes if n == 1)
        return max(N-leaf_cnt-1, 0)


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

        p = IntArray().Input(N)

        obj = Solution()
        res = obj.solve(N, p)

        print(res)


# } Driver Code Ends
