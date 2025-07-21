# Problem Statement: https://www.geeksforgeeks.org/problems/critical-connections/1

#User function Template for python3

time=0
class Solution:
    def dfs_mod(self,u,adj,visited,disc,low,bridge,parent):
        visited[u]=True
        global time
        disc[u]=time
        low[u]=time
        time+=1
        for v in adj[u]:
            if visited[v]==False:
                self.dfs_mod(v,adj,visited,disc,low,bridge,u)
                low[u]=min(low[u],low[v])
                if low[v]>disc[u]:
                    bridge.append(sorted([u,v]))
            elif v!=parent:
                low[u]=min(low[u],disc[v])

    def criticalConnections(self, v, adj):
        visited=[False]*v
        disc=[0]*v
        low=[0]*v
        bridge=[]
        self.dfs_mod(0,adj,visited,disc,low,bridge,-1)
        bridge.sort()
        return bridge


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.criticalConnections(V, adj)
		for i in range(len(ans)):
		    print(ans[i][0],ans[i][1])

# } Driver Code Ends