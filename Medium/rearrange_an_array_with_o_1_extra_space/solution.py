# Problem Statement: https://practice.geeksforgeeks.org/problems/rearrange-an-array-with-o1-extra-space3142/1

# User function Template for python3

# Complete this code

import math


class Solution:
    # Function to rearrange an array so that arr[i] becomes arr[arr[i]]
    # with O(1) extra space.
    def arrange(self, arr, n):
        # Your code here
        for i in range(n):
            v = arr[arr[i]] % n
            arr[i] += v*n

        for i in range(n):
            arr[i] //= n
        return arr

# {
 # Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        ob.arrange(arr, n)

        for i in arr:
            print(i, end=" ")

        print()

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
