# Problem Statement: https://practice.geeksforgeeks.org/problems/nodes-at-even-distance0532/1

#User function Template for python3
from collections import deque

class Solution:
    def countOfNodes(self, graph,n):
        vis = set()
        dist = [-1]*(n+1)
        q = deque([1])
        dist[1] = 0
        vis.add(1)
        while q:
            x = q.popleft()
            for i in graph[x]:
                if i not in vis:
                    dist[i] = dist[x]+1
                    vis.add(i)
                    q.append(i)

        a = b = 0
        for i in range(1,len(dist)):
            x = dist[i]
            if x ==-1:
                continue
            if x&1==0:
                a += 1
            else:
                b += 1

        return (a*(a-1)+ b*(b-1))//2

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        arr = input().split()
        graph = defaultdict(list)
        for i in range(0,2*n-2,2):
            graph[int(arr[i])].append(int(arr[i+1]))
            graph[int(arr[i+1])].append(int(arr[i]))
            
            
        
        ob = Solution()
        print(ob.countOfNodes(graph,n))
# } Driver Code Ends