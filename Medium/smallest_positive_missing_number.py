# Problem Statement: https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1

# User function Template for python3

import math


class Solution:

    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr, n):
        # Your code here
        d = {}
        for i in arr:
            d[i] = 1

        i = 1
        while (True):
            if i not in d:
                return i
            i += 1


# {
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        print(ob.missingNumber(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
