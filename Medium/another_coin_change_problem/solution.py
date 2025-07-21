# Problem Statement: https://practice.geeksforgeeks.org/problems/09b910559335521654aa2909f86f893447d8f5ba/1

from typing import List


class Solution:
    def makeChanges(self, N: int, k: int, target: int, coins: List[int]) -> bool:
        dp = [[0]*(k+1) for _ in range(target+1)]
        dp[0][0] = 1
        coins.sort()
        for t in range(target):
            for n in range(k):
                for coin in coins:
                    if t+1-coin < 0:
                        break
                    dp[t+1][n+1] += dp[t+1-coin][n]

        return dp[target][k]


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

        K = int(input())

        target = int(input())

        coins = IntArray().Input(N)

        obj = Solution()
        res = obj.makeChanges(N, K, target, coins)

        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends
