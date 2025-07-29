# Problem Statement: https://practice.geeksforgeeks.org/problems/eventual-safe-states/1

#User function Template for python3

from typing import List
import copy


class Solution:
    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        from collections import defaultdict
        indegree = [0]*V
        rg = defaultdict(list)
        
        for frm, r in enumerate(adj):
            for to in r:
                rg[to].append(frm)
                indegree[frm] += 1
        
        q = []
        for i, e in enumerate(indegree):
            if e == 0:
                q.append(i)
        ans = []
        while q:
            e = q.pop()
            ans.append(e)
            for nbr in rg[e]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
        return sorted(ans)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends