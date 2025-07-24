# Problem Statement: https://practice.geeksforgeeks.org/problems/234ca3b438298fb04befd5abe7fbd98c006d4884/1

#User function Template for python3

from collections import deque
class Solution():
    def bfs(self, mat, n, m, src):
        Q = deque(src)
        visited = set(src)
        while Q:
            x, y = Q.popleft()
            for nx, ny in [[x, y+1], [x, y-1], [x+1, y], [x-1, y]]:
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] >= mat[x][y] and (nx,ny) not in visited:
                    Q.append((nx, ny))
                    visited.add((nx,ny))
        return visited
            
        
    def water_flow(self, mat, n, m):
        visited1 = self.bfs(mat, n, m, [(i,0) for i in range(n)] + [(0,j) for j in range(m)])
        visited2 = self.bfs(mat, n, m, [(i,m-1) for i in range(n)] + [(n-1,j) for j in range(m)])
        return len(visited1 & visited2)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == "__main__":
    for _ in range(int(input())):
        n,m = map(int, input().split())
        mat = []
        for i in range(n):
            tmp = [int(i) for i in input().split()]
            mat.append(tmp)
        print(Solution().water_flow(mat, n, m))
# } Driver Code Ends