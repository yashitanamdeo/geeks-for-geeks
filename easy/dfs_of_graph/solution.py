# Problem Statement: https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

# User function Template for python3

class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def traverse(self, s, adj, visited, res):
        res.append(s)
        visited[s] = True
        for e in adj[s]:
            if visited[e] == False:
                self.traverse(e, adj, visited, res)

    def dfsOfGraph(self, V, adj):
        visited = [False]*V
        res = []
        self.traverse(0, adj, visited, res)
        return res

# {
 # Driver Code Starts


if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        adj = [[] for i in range(V+1)]
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
# } Driver Code Ends
