# Problem Statement: https://practice.geeksforgeeks.org/problems/5a1277ffc1ec1d3a63d1a5d6b3920dd3d1294261/1

#User function Template for python3
from typing import List
from collections import deque


class Solution:
    def chefAndWells(self, n: int, m: int, c: List[List[str]]) -> List[List[int]]:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[False] * m for i in range(n)]
        dist = [[-1] * m for i in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if c[i][j] == 'W':
                    q.append([i, j])
                    visited[i][j] = True
                if c[i][j] == 'W' or c[i][j] == '.' or c[i][j] == 'N':
                    dist[i][j] = 0

        dis = 2
        while q:
            size = len(q)
            for p in range(size):
                x = q.popleft()
                i = x[0]
                j = x[1]
                for k in range(4):
                    curri = i + dx[k]
                    currj = j + dy[k]

                    if curri >= 0 and currj >= 0 and curri < n and currj < m and visited[curri][currj] == False and c[curri][currj] != 'N':
                        visited[curri][currj] = True
                        q.append([curri, currj])
                        if c[curri][currj] == 'H':
                            dist[curri][currj] = dis

            dis += 2

        return dist


#{
 # Driver Code Starts
#Initial Template for Python 3


class StringMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([i for i in input().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
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

        n, m = map(int, input().split())

        c = StringMatrix().Input(n, m)

        obj = Solution()
        res = obj.chefAndWells(n, m, c)

        for el in res:
            for c in el:
                print(c, end=" ")
            print()

# } Driver Code Ends
