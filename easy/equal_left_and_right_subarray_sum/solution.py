# Problem Statement: https://practice.geeksforgeeks.org/problems/78a6854c8a2915e05f236aa407dfaa1bbc8ae7d3/1

# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
   def equalSum(self,A, N):
        s, running = sum(A), 0
        for i, e in enumerate(A):
            if running == s-running-e:
                return i+1
            running += e
        return -1



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equalSum(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends