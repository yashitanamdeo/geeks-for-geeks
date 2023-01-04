# Problem Statement: https://practice.geeksforgeeks.org/problems/649205908e04ac00f303626fa845261318adfa8f/1

from typing import List


class Solution:

    def maximum_profit(self, n: int, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        M = intervals[-1][1]
        dp = [0]*(M+1)

        for i in range(n):
            s, e, p = intervals[i]
            if p+dp[s] > dp[e]:
                dp[e] = p+dp[s]
            if i < n-1:
                _, en, _ = intervals[i+1]
                for j in range(e+1, en+1):
                    dp[j] = dp[e]

        return dp[M]


#{
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
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

        intervals = IntMatrix().Input(n, 3)

        obj = Solution()
        res = obj.maximum_profit(n, intervals)

        print(res)


# } Driver Code Ends
