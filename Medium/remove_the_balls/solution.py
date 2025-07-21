# Problem Statement: https://practice.geeksforgeeks.org/problems/546ea68f97be7283a04ddcc8057e09b46a686471/1

from typing import List


class Solution:
    def finLength(self, N: int, color: List[int], radius: List[int]) -> int:
        stk = [[color[0], radius[0]]]
        for i in range(1, N):
            if len(stk) > 0:
                if stk[-1][0] == color[i] and stk[-1][1] == radius[i]:
                    stk.pop()
                else:
                    stk.append([color[i], radius[i]])
            else:
                stk.append([color[i], radius[i]])
        return len(stk)


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

        color = IntArray().Input(N)

        radius = IntArray().Input(N)

        obj = Solution()
        res = obj.finLength(N, color, radius)

        print(res)


# } Driver Code Ends
