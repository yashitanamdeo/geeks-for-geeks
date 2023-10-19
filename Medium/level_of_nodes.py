# Problem Statement: https://practice.geeksforgeeks.org/problems/level-of-nodes-1587115620/1

# User function Template for python3
from collections import deque


class Solution:

    # Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        q = deque()
        q.append(0)
        visited = [False]*V
        visited[0] = True
        level = 0
        while q:
            for i in range(len(q)):
                u = q.popleft()
                if u == X:
                    return level
                for v in adj[u]:
                    if visited[v] == False:
                        visited[u] = True
                        q.append(v)
            level += 1
        return -1


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V, E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a, b = map(int, input().strip().split())
            adj[a].append(b)
            adj[b].append(a)
        X = int(input())
        ob = Solution()

        print(ob.nodeLevel(V, adj, X))
# } Driver Code Ends
