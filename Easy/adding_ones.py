# Problem Statement: https://practice.geeksforgeeks.org/problems/adding-ones3628/1

# User function Template for python3

from collections import Counter


class Solution:
    def update(self, a, n, updates, k):
        d = Counter(updates)
        a[0] = d[1]
        for x in range(1, n):
            a[x] = d[x+1] + a[x-1]
        return a


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    T = int(input())

    while (T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [0 for i in range(n)]
        updates = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.update(a, n, updates, k)
        print(*a)

        T -= 1


# } Driver Code Ends
