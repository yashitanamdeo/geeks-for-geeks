# Problem Statement: https://practice.geeksforgeeks.org/problems/stock-buy-and-sell2615/1


from typing import List


class Solution:
    def stockBuyAndSell(self, n: int, prices: List[int]) -> int:
        # code here
        ans = 0
        b = prices[0]
        i = 1
        while i < n:
            if prices[i] <= b:
                b = prices[i]
            else:
                if i+1 < n and prices[i+1] >= prices[i]:
                    pass
                else:
                    ans += prices[i]-b
                    if i+1 < n:
                        b = prices[i+1]
            i += 1
        return ans


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

        prices = IntArray().Input(n)

        obj = Solution()
        res = obj.stockBuyAndSell(n, prices)

        print(res)


# } Driver Code Ends
