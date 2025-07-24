# Problem Statement: https://practice.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1

# {
# Driver Code Starts
# Initial Template for Python 3

import math


# } Driver Code Ends
# User function Template for python3


class Solution:
    def checkKthBit(self, n, k):
        return (n & (1 << k))


# {
 # Driver Code Starts.


def main():

    T = int(input())

    while (T > 0):

        n = int(input())
        k = int(input())
        obj = Solution()
        if obj.checkKthBit(n, k):
            print("Yes")
        else:
            print("No")

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
