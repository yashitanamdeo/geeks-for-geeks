# Problem Statement: https://practice.geeksforgeeks.org/problems/number-of-open-doors1552/1

#User function Template for python3

import math


class Solution:
    def noOfOpenDoors(self, N):
        # code here
        return int(N**(1/2))


#{
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.noOfOpenDoors(N))
# } Driver Code Ends
