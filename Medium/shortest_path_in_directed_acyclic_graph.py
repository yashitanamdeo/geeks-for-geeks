# Problem Statement: https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1

# User function Template for python3

from typing import List


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        from heapq import heappush, heappop
        from collections import defaultdict

        g = defaultdict(list)
        for frm, to, cost in edges:
            g[frm].append((to, cost))

        costs = [-1]*n
        costs[0] = 0

        q = [(0, 0)]
        while q:
            cost0, v = heappop(q)
            for to, dc in g[v]:
                cost = cost0+dc
                if costs[to] == -1 or costs[to] > cost:
                    heappush(q, (cost, to))
                    costs[to] = cost
        return costs

# {
 # Driver Code Starts

# Initial Template for Python 3


class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n, m = map(int, input().split())

        edges = IntMatrix().Input(m, 3)

        obj = Solution()
        res = obj.shortestPath(n, m, edges)

        IntArray().Print(res)
# } Driver Code Ends
