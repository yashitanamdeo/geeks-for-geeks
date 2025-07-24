# Problem Statement: https://practice.geeksforgeeks.org/problems/1132bd8ee92072cd31441858402641d6800fa6b3/1

import math


class Solution:
    def countBits(self, N: int) -> int:
        if (N <= 1):
            return N
        x = math.floor(math.log2(N))
        return x*(1 << (x-1)) + (N - (1 << x) + 1) + self.countBits(N - (1 << x))


# {
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        N = int(input())

        obj = Solution()
        res = obj.countBits(N)

        print(res)


# } Driver Code Ends
