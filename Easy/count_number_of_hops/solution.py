# Problem Statement: https://practice.geeksforgeeks.org/problems/count-number-of-hops-1587115620/1

# User function Template for python3

import sys
import io
import atexit


class Solution:
    # Function to count the number of ways in which frog can reach the top.
    def countWays(self, n):
        jumps = [1, 2, 3]
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        a, b, res = 1, 2, 4
        for _ in range(n-3):
            val = (res+a+b) % (10**9+7)
            a, b, res = b, res, val
        return val


# {
 # Driver Code Starts
# Initial Template for Python 3
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))
# } Driver Code Ends
