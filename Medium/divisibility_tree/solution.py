# Problem Statement: https://www.geeksforgeeks.org/problems/divisibility-tree1902/1


from typing import List


class Solution:
    ans=None

    def dfs(self,adj,u,parent):
        res=0
        for v in adj[u]:
            if v!=parent:
                val=self.dfs(adj,v,u)
                res+=val
                if val%2==0:
                    self.ans+=1
        return res+1
    
    def minimumEdgeRemove(self,n,edges):
        self.ans=0
        adj=[[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        self.dfs(adj,1,-1)
        return self.ans
        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
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

        n = int(input())

        edges = IntMatrix().Input(n - 1, 2)

        obj = Solution()
        res = obj.minimumEdgeRemove(n, edges)

        print(res)

# } Driver Code Ends