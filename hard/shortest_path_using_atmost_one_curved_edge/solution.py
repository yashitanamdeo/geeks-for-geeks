# Problem Statement: https://practice.geeksforgeeks.org/problems/e7d81a082cda6bd1e959d943197aa3bc21b88bdb/1

#User function Template for python3

class Solution:
    def shortestPath(self, n, m, a, b, edges):
        from collections import defaultdict
        g = defaultdict(list)
        for (x, y, w1, w2) in edges:
            g[x].append((y, w1, w2))
            g[y].append((x, w1, w2))
            

        costs = {(a, -1): 0}
        q = [(0, -1, a)]
        
        while q:
            cost, k, node = heappop(q)
            if node == b:
                return cost
            for nbr, w1, w2 in g[node]:
                scost = cost+w1
                ccost = cost+w2
                
                if k == 0:
                    if (nbr, 0) in costs and costs[nbr, 0] < scost:
                        continue
                    if (nbr, -1) in costs and costs[nbr, -1] <= scost:
                        continue
                    costs[nbr, 0] = scost
                    heappush(q, (scost, 0, nbr))

                else:
                    # not use curved
                    if (nbr, -1) not in costs or costs[nbr, -1] > scost:
                        costs[nbr, -1] = scost
                        heappush(q, (scost, -1, nbr))
                    if (nbr, 0) not in costs or costs[nbr, 0] > ccost:
                        if (nbr, -1) not in costs or costs[nbr, -1] > ccost:
                            costs[nbr, 0] = ccost
                            heappush(q, (ccost, 0, nbr))
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys 
sys.setrecursionlimit(10**6) 
from heapq import *

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,m=map(int,input().split())
        a,b=map(int,input().split())
        edges = []
        for i in range(m):
            edge = list(map(int,input().split()))
            edges.append(edge)
        
        ob = Solution()
        print(ob.shortestPath(n,m,a,b,edges))
# } Driver Code Ends