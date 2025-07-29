# Problem Statement: https://practice.geeksforgeeks.org/problems/maximum-sum-lcm3025/1

# User function Template for python3
import math


class Solution:

    def maxSumLCM(self, n):
        # c o de here
        sum = 0
        for i in range(1, int(math.sqrt(n)+1)):
            if n % i == 0:
                if i == (n//i):
                    sum += i
                else:
                    sum += i
                    sum += n//i
        return sum


# {
 # Driver Code Starts
# Initial Template for Pyton 3
if __name__ == '__ain__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.maxSumLCM(n))
# } Driver Code Ends
