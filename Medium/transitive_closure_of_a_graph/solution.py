# Problem Statement: https://practice.geeksforgeeks.org/problems/transitive-closure-of-a-graph0930/1

# User function Template for python3

class Solution:
    def transitiveClosure(self, N, graph):
        # code here

        adj = [[] for i in range(N)]

        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1:
                    if i != j:
                        adj[i].append(j)

        ans = [[0 for i in range(N)] for j in range(N)]

        def dfs(r, i, visit):
            ans[r][i] = 1
            visit.add(i)
            for ele in adj[i]:
                if ele not in visit:
                    dfs(r, ele, visit)

        for i in range(N):
            dfs(i, i, set())
        return ans


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        graph = []
        for i in range(0, N):
            graph.append([int(j) for j in input().split()])
        ob = Solution()
        ans = ob.transitiveClosure(N, graph)
        for i in range(N):
            for j in range(N):
                print(ans[i][j], end=" ")
            print()
# } Driver Code Ends
