# Problem Statement: https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1

import math


class Solution:

    def frequencyCount(self, arr, n, p):
        # Step 1: Identify and ignore elements greater than N
        for i in range(n):
            if arr[i] > n:
                arr[i] = 0

        # Step 2: Encode frequency information into array elements
        for i in range(n):
            if arr[i] % (n + 1) > 0:
                arr[(arr[i] % (n + 1)) - 1] += (n + 1)

        # Step 3: Decode the frequency information
        for i in range(n):
            arr[i] //= (n + 1)


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    T = int(input())
    while (T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        P = int(input())
        ob = Solution()
        ob.frequencyCount(arr, N, P)
        for i in arr:
            print(i, end=" ")
        print()
        T -= 1


# } Driver Code Ends
