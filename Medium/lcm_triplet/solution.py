# Problem Statement: https://practice.geeksforgeeks.org/problems/lcm-triplet1501/1

#User function Template for python3

import math


class Solution:
    def lcmTriplets(self, N):
        #code here
        if N <= 2:
            return N
        if (N & 1) == 1:
            return N*(N-1)*(N-2)
        if N % 3 == 0:
            return (N-2)*(N-1)*(N-3)
        return N*(N-1)*(N-3)

class Solution1: 
    def lcmTriplets(self, n):
        if n<3:
            return n
        if n%2:
            return n*(n-1)*(n-2)
        if n%3:
            return n*(n-1)*(n-3)
        return (n-1)*(n-2)*(n-3)

#{
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.lcmTriplets(N))
# } Driver Code Ends
