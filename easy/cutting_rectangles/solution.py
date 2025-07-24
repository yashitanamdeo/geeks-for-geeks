# Problem Statement: https://practice.geeksforgeeks.org/problems/a7a4da81b20f4a05bbd93f5786fcf7478298f4f5/1

#User function Template for python3

import math


class Solution:
    def minimumSquares(self, L, B):
        # code here
        gcd = math.gcd(L, B)
        return [(L // gcd) * (B // gcd), gcd]


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, B = [int(x) for x in input().split()]

        ob = Solution()
        N, K = ob.minimumSquares(L, B)
        print(N, end=" ")
        print(K)
# } Driver Code Ends
