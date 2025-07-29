# Problem Statement: https://www.geeksforgeeks.org/problems/is-it-a-tree/1

#User function Template for python3

class Solution:
    def dfs(self,adj,s):
        n=len(adj)
        visited=[False]*n
        stack=[(s,-1)]
        visited[s]=True
        while stack:
            u,parent=stack.pop()
            for v in adj[u]:
                if visited[v]==False:
                    stack.append((v,u))
                    visited[v]=True
                elif v!=parent:
                    return 0
        if False in visited:
            return 0
        return 1
    
    def isTree(self, n, m, edges):
        adj=[[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        return self.dfs(adj,0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range (int(input())):
    n,m = [int(i) for i in input().split()]
    edges = []
    for i in range(m):
        a,b = map(int,input().split())
        edges.append([a,b])

    ob = Solution()
    print(ob.isTree(n,m,edges))
# } Driver Code Ends