# Problem Statement: https://practice.geeksforgeeks.org/problems/power-of-2-1587115620/1

# User function Template for python3

import math


class Solution:
    # Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        return n & -n == n and n != 0


# {
 # Driver Code Starts
# Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        n = int(input())
        ob = Solution()
        if ob.isPowerofTwo(n):
            print("YES")
        else:
            print("NO")

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
