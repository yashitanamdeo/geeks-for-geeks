# Problem Statement: https://www.geeksforgeeks.org/problems/rightmost-different-bit-1587115621/1

# {
# Driver Code Starts
# Initial Template for Python 3

import math


# } Driver Code Ends
# User function Template for python3

class Solution:
    def posOfRightMostDiffBit(self, m, n):
        # XOR of two numbers will give a number with set bits at the different positions.
        xor_result = m ^ n

        # If the numbers are the same, return -1.
        if xor_result == 0:
            return -1

        # Find the position of the rightmost set bit in the XOR result.
        position = 1
        while xor_result:
            if xor_result & 1:
                return position
            xor_result >>= 1
            position += 1

        # This line should not be reached, as there must be a different bit.
        return -1

# {
 # Driver Code Starts.


def main():

    T = int(input())

    while (T > 0):

        mn = [int(x) for x in input().strip().split()]
        m = mn[0]
        n = mn[1]
        ob = Solution()
        print(math.floor(ob.posOfRightMostDiffBit(m, n)))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
