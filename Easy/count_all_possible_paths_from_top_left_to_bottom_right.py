# Problem Statement: https://practice.geeksforgeeks.org/problems/count-all-possible-paths-from-top-left-to-bottom-right3011/1

# User function Template for python3
import math


class Solution:
    def numberOfPaths(self, m, n):

        # code here

    a = math.factorial(m+n-2)
    b = math.factorial(n-1)
    c = math.factorial(m-1)

    d = b*c
    return (a//d) % 1000000007


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        m, n = input().split()
        m = int(m)
        n = int(n)
        ob = Solution()
        print(ob.numberOfPaths(m, n))

# } Driver Code Ends
