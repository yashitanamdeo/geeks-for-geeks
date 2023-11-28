# Problem Statement: https://www.geeksforgeeks.org/problems/sum-of-dependencies-in-a-graph5311/1

#User function Template for python3

class Solution:
    def sumOfDependencies(self, adjacency_list, num_vertices):
        total_dependencies = 0

        # Iterate through each vertex in the adjacency list
        for neighbors in adjacency_list:
            # Add the number of dependencies for the current vertex
            total_dependencies += len(neighbors)

        return total_dependencies


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split())
        a=[[] for i in range(N)]
        s=list(map(int,input().strip().split()))
        for i in range(0,2*M,2):
            x=s[i]
            y=s[i+1]
            a[x].append(y)
        ob=Solution()
        print(ob.sumOfDependencies(a,N))
        


# } Driver Code Ends