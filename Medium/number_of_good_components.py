# Problem Statement: https://practice.geeksforgeeks.org/problems/1a4b617b70f0142a5c2b454e6fbe1b9a69ce7861/1

# User function Template for python3

from sys import stdin, stdout
import collections
from collections import deque
from collections import defaultdict


class Solution:
    def findNumberOfGoodComponent(self, V, adj):
        def solve(node, isVisited):
            if node in isVisited:
                return 0, 0
            isVisited.add(node)
            res = 0
            totalnode = 1
            for child in adj[node]:
                val, data = solve(child, isVisited)
                res = 1+val+res
                totalnode += data
            return res, totalnode

        res = 0
        isVisited = set()
        for i in range(1, V+1):
            if i not in isVisited:
                val = solve(i, isVisited)
                if (val[1]*(val[1]-1) == val[0]):
                    res += 1
        return res


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for _ in range(test_cases):
        E, V = map(int, input().split())
        adj = [[] for _ in range(V+1)]
        for _ in range(E):
            a, b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)

        res = Solution().findNumberOfGoodComponent(V, adj)
        print(res)
# } Driver Code Ends
