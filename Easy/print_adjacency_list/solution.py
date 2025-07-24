# Problem Statement: https://practice.geeksforgeeks.org/problems/print-adjacency-list-1587115620/1


from typing import List


class Solution:
    def printGraph(self, V: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[]] * V
        for i in range(len(edges)):
            adj[edges[i][0]] = ([*adj[edges[i][0]], edges[i][1]])
            adj[edges[i][1]] = ([*adj[edges[i][1]], edges[i][0]])
        # print(adj)
        return adj
        # code here


# {
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


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

        V, E = IntArray().Input()

        edges = IntMatrix().Input(E, 2)

        obj = Solution()
        res = obj.printGraph(V, edges)

        for row in res:
            print(*sorted(row))
# } Driver Code Ends
