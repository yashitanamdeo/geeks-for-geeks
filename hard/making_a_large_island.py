# Problem Statement: https://practice.geeksforgeeks.org/problems/making-a-large-island/1

from typing import List


class Solution:
    def largestIsland(self, l: List[List[int]]) -> int:
        k, s = [], {}
        c, h = 2, 0
        n, m = len(l), len(l[0])

        def dfs(i, j, c):
            if l[i][j] == 1:
                l[i][j] = c
                s[c] += 1
            if j < m-1 and l[i][j+1] == 1:
                dfs(i, j+1, c)
            if i < n-1 and l[i+1][j] == 1:
                dfs(i+1, j, c)
            if j > 0 and l[i][j-1] == 1:
                dfs(i, j-1, c)
            if i > 0 and l[i-1][j] == 1:
                dfs(i-1, j, c)
        for i in range(n):
            for j in range(m):
                if isinstance(l[i][j], int) and l[i][j] == 1:
                    s[c] = 0
                    dfs(i, j, c)
                    h = max(h, s[c]+1)
                    c += 1
        if h == 0:
            return (1)

        def count(i, j):
            c, k = 0, set()
            if j < m-1 and l[i][j+1] > 1 and l[i][j+1] not in k:
                k.add(l[i][j+1])
                c += s[l[i][j+1]]
            if i < n-1 and l[i+1][j] > 1 and l[i+1][j] not in k:
                k.add(l[i+1][j])
                c += s[l[i+1][j]]
            if j > 0 and l[i][j-1] > 1 and l[i][j-1] not in k:
                k.add(l[i][j-1])
                c += s[l[i][j-1]]
            if i > 0 and l[i-1][j] > 1 and l[i-1][j] not in k:
                k.add(l[i-1][j])
                c += s[l[i-1][j]]
            return (c)
        for i in range(n):
            for j in range(m):
                if l[i][j] == 0:
                    h = max(count(i, j)+1, h)
        return (min(h, m*n))


# {
 # Driver Code Starts

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


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        grid = IntMatrix().Input(n, n)

        obj = Solution()
        res = obj.largestIsland(grid)

        print(res)
# } Driver Code Ends
