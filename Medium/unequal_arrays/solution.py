# Problem Statement: https://practice.geeksforgeeks.org/problems/4db2fcd97400456c4914d5a3e8ad932cc21e3e9d/1

from typing import List


class Solution:
    def solve(self, N: int, A: List[int], B: List[int]) -> int:
        # code here
        if sum(A) != sum(B):
            return -1
        oa = []
        ea = []
        ob = []
        eb = []
        for i in A:
            if i % 2:
                oa.append(i)
            else:
                ea.append(i)
        for i in B:
            if i % 2:
                ob.append(i)
            else:
                eb.append(i)
        if len(oa) != len(ob) or len(ea) != len(eb):
            return -1
        oa.sort()
        ea.sort()
        ob.sort()
        eb.sort()
        ans = 0
        for i in range(len(oa)):
            x = abs(oa[i]-ob[i])
            ans += (x//2)
        for i in range(len(eb)):
            x = abs(eb[i]-ea[i])
            ans += (x//2)

        return ans//2


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

        B = IntArray().Input(N)

        obj = Solution()
        res = obj.solve(N, A, B)

        print(res)


# } Driver Code Ends
