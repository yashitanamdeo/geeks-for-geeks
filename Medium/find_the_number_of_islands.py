# Problem Statement: https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1#

#User function Template for python3
from queue import Queue

class Solution:
    def bfs(self, grid, i, j, n, m):
       
        q = Queue()
        q.put((i, j))
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1))
       
        grid[i][j] = 0
       
        while not q.empty():
            x, y = q.get()
           
            for dir in directions:
                dx, dy = dir
                if x + dx < 0 or y + dy < 0 or x + dx >= n or y + dy >= m or grid[x + dx][y + dy] == 0:
                    continue
                q.put((x + dx, y + dy))
                grid[x + dx][y + dy] = 0
               
   
    def numIslands(self,grid):
        n = len(grid)
        m = len(grid[0])
       
        c = 0
       
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, n, m)
                    c += 1
        return c
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends