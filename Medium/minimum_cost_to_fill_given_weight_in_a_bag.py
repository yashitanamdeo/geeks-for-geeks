# Problem Statement: https://www.geeksforgeeks.org/problems/minimum-cost-to-fill-given-weight-in-a-bag1956/1


from typing import List
class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        dp = [float('inf')] * (w + 1);
        dp[0] = 0
        
        for i in range(n):
            for j in range(i + 1, w + 1):
                dp[j] = min(dp[j], cost[i] + dp[j - i - 1])
            
        return dp[w]



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        w = int(input())

        cost = IntArray().Input(n)

        obj = Solution()
        res = obj.minimumCost(n, w, cost)

        print(res)

# } Driver Code Ends