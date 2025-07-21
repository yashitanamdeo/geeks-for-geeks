# Problem Statement: https://www.geeksforgeeks.org/problems/grinding-geek/1


from typing import List


class Solution:
    def max_courses(self, n: int, total: int, cost: List[int]) -> int:
        # code here

        from math import floor

        dp = [[None]*len(cost) for _ in range(total+1)]

        def compute(i, total):
            nonlocal cost, n, dp
            if i >= len(cost):
                return 0
            if dp[total][i] is not None:
                return dp[total][i]
            c1 = compute(i+1, total)

            if total < cost[i]:
                dp[total][i] = c1
                return c1

            rcost = cost[i]
            if i < n:
                rcost -= floor(cost[i]*0.9)

            dp[total][i] = max(c1, compute(i+1, total-rcost)+1)
            return dp[total][i]

        return compute(0, total)


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

        total = int(input())

        cost = IntArray().Input(n)

        obj = Solution()
        res = obj.max_courses(n, total, cost)

        print(res)


# } Driver Code Ends
