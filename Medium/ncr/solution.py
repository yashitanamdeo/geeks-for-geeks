# Problem Statement: https://practice.geeksforgeeks.org/problems/ncr1019/1

# User function Template for python3

import sys
facto = [1]
for i in range(1, 1001):
    facto.append(facto[~0] * i)


class Solution:
    def nCr(self, n, r):
        return (facto[n] // (facto[r] * facto[n - r])) % (10 ** 9 + 7)


# {
 # Driver Code Starts
# Initial Template for Python 3

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends
