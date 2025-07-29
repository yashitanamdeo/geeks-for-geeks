# Problem Statement: https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1#

class Solution:

   #Function to find the shortest distance of all the vertices
   #from the source vertex S.
    def dijkstra(self, V, adj, S):
        result = [sys.maxsize] * V
        result[S] = 0
        queue = []
        queue.append(S)
        while queue:
            vertex = queue.pop(0)
            for neighbour in adj[vertex]:
                adj_vertex = neighbour[0]
                adj_distance = neighbour[1]
                if result[vertex] + adj_distance < result[adj_vertex]:
                    result[adj_vertex] = result[vertex] + adj_distance
                    queue.append(adj_vertex)
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends