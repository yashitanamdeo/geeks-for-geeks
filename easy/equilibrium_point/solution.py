# Problem Statement: https://practice.geeksforgeeks.org/problems/equilibrium-point-1587115620/1

# User function Template for python3

import math


class Solution:
    def equilibriumPoint(self, A, N):
        if N == 1:
            return 1
        sum = 0
        sumans = 0
        for i in range(N):
            sum += A[i]
        for i in range(N):
            sum -= A[i]
            if sum == sumans:
                return i+1
            sumans += A[i]
        return -1


# {
 # Driver Code Starts
# Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
