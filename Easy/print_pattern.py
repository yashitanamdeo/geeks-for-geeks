# Problem Statement: https://www.geeksforgeeks.org/problems/print-pattern3549/1

# User function Template for python3

import sys
sys.setrecursionlimit((10**5)//5)


class Solution:
    def help(self, n, l):
        l.append(n)
        if n > 0:
            self.help(n-5, l)
            l.append(n)

    def pattern(self, N):
        l = []
        self.help(N, l)
        return l


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends
