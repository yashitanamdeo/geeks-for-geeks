# Problem Statement: https://www.geeksforgeeks.org/problems/geekina-hate-1s/1

from typing import List
from math import log2, factorial


class Solution:
    def comb(self, n, r):
        return factorial(n)//(factorial(r) * factorial(n-r)) if n >= r else 0

    def count_exact(self, a, k):
        if k == 0:
            return 1
        if a == 0:
            return 0
        m = int(log2(a))
        if m < k-1:
            return 0
        return self.comb(m, k) + self.count_exact(a ^ (1 << m), k-1)

    def count(self, a, k):
        return sum(self.count_exact(a, i) for i in range(k+1))

    def findNthNumber(self, n: int, k: int) -> int:
        lo, hi = 0, 10**18
        while lo < hi:
            mid = lo + (hi - lo)//2
            if self.count(mid, k) >= n:
                hi = mid
            else:
                lo = mid + 1
        return lo


# {
 # Driver Code Starts


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n, k = map(int, input().split())

        obj = Solution()
        res = obj.findNthNumber(n, k)

        print(res)


# } Driver Code Ends
