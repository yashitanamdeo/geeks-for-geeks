# Problem Statement: https://practice.geeksforgeeks.org/problems/cec5db442a5652d07dd41e37ea780345f08c9a3d/1

from typing import List


class Solution:
    def goodSubsets(self, n: int, arr: List[int]) -> int:
        from functools import reduce
        MOD = 10**9+7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        A = [0]*31
        for v in arr:
            A[v] += 1
        # process valid composites numbers
        def exc(*ex): return [v for v in primes if v not in ex and A[v] > 0]
        mp = {
            (6,): exc(2, 3), (10,): exc(2, 5), (14,): exc(2, 7),
            (15,): exc(3, 5), (15, 14): exc(2, 3, 5, 7),
            (21,): exc(3, 7), (21, 10): exc(2, 3, 5, 7),
            (22,): exc(2, 11), (22, 15): exc(2, 3, 5, 11), (22, 21): exc(2, 3, 7, 11),
            (26,): exc(2, 13), (26, 15): exc(2, 3, 5, 13), (26, 21): exc(2, 3, 7, 13),
            (30,): exc(2, 3, 5)
        }
        ans = 0
        for v in primes:
            ans = (ans + A[v] * (1+ans)) % MOD
        for cvs, targets in mp.items():
            if any(A[v] == 0 for v in cvs):
                continue
            prod = reduce(lambda a, b: (a*b) % MOD, (A[v] for v in cvs))
            tmp = 0
            for v in targets:
                tmp = (tmp + A[v] * (1 + tmp)) % MOD
            ans = (ans + (tmp+1)*prod) % MOD

        K1 = pow(2, A[1], MOD)  # \sum_{i=0}^{n} \binom{n}{i}
        ans = (ans * K1) % MOD
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

        n = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.goodSubsets(n, arr)

        print(res)


# } Driver Code Ends
