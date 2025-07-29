# Problem Statement: https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1

# User function Template for python3

import sys
import io
import atexit


class Solution:

    # Function to find the maximum money the thief can get.
    def FindMaxSum(self, a, n):

        # code here
        if n == 0:
            return
        if n == 1:
            return a[0]
        if n == 2:
            return max(a[0], a[1])
        dp = [0]*n
        dp[0] = a[0]
        dp[1] = max(a[0], a[1])
        for i in range(2, n):
            dp[i] = max(a[i]+dp[i-2], dp[i-1])
        return dp[n-1]


# {
 # Driver Code Starts
# Initial Template for Python 3
sys.setrecursionlimit(10**6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.FindMaxSum(a, n))
# } Driver Code Ends
