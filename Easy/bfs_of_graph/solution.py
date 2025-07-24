# Problem Statement: https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

# User function Template for python3

from typing import List
from queue import Queue


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visit = [0 for i in range(V)]  # making visit matrix of len v =0
        ans = [0]  # taking first vertex in to solution
        q = [0]  # using first vertex in q for bfs
        visit[0] = 1  # making first vertex 1
        while len(q) != 0:
            j = 0
            curr = q[0]
            q.remove(q[0])
            while j < len(adj[curr]):
                if adj[curr][j] != None and visit[adj[curr][j]] != 1:
                    ans.append(adj[curr][j])
                    visit[adj[curr][j]] = 1
                    q.append(adj[curr][j])
                j += 1
        return ans

# {
 # Driver Code Starts


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()


# } Driver Code Ends
