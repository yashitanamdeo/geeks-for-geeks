# Problem Statement: https://www.geeksforgeeks.org/problems/vertex-cover/1

from typing import List


class Solution:
    def help(self, adj, i, visited, e):
        n = len(adj)
        
        # Base case: If no edges remaining, return the count of visited vertices
        if e == 0:
            return visited.count(True)
        
        # Base case: If all vertices have been considered, return infinity
        if i == n:
            return float("inf")
        
        # Count the number of unvisited neighbors of the current vertex
        c = sum(1 for v in adj[i] if not visited[v])
        
        # Include the current vertex in the cover
        visited[i] = True
        x = self.help(adj, i + 1, visited, e - c)
        
        # Backtrack: Exclude the current vertex from the cover
        visited[i] = False
        y = self.help(adj, i + 1, visited, e)
        
        # Return the minimum size of the vertex cover
        return min(x, y)

    def vertexCover(self, n, edges):
        e = len(edges)
        
        # Create an adjacency list for the graph
        adj = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj[v1 - 1].append(v2 - 1)
            adj[v2 - 1].append(v1 - 1)
        
        # Initialize a visited array to track included vertices in the cover
        visited = [False] * n
        
        # Call the helper function to find the minimum size of the vertex cover
        return self.help(adj, 0, visited, e)

        



#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        
        edges=IntMatrix().Input(m, m)
        
        obj = Solution()
        res = obj.vertexCover(n, edges)
        
        print(res)
        

# } Driver Code Ends