# Problem Statement: https://practice.geeksforgeeks.org/problems/eulerian-path-in-an-undirected-graph5052/1

# User function Template for Python3

class Solution:
    def eulerPath(self, N, graph):
        # code 
        # for eulerian path, the (N-2) vertices must have degrees(indegree + outdegree) as even
        # if all even than it will be eulerian circuit
        evencount = 0
        for i in range(N):
            if sum(graph[i]) %2 ==0:
                evencount+=1
        if evencount == (N-2):
            return 1
        return 0

#{ 
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        graph = []
        for i in range(N):
            graph.append(list(map(int, input().strip().split())))
        
        ob = Solution()
        print(ob.eulerPath(N, graph))
# } Driver Code Ends