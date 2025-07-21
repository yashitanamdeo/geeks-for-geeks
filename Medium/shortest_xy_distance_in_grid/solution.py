# Problem Statement: https://practice.geeksforgeeks.org/problems/7366ce450d84b55391fc787a681c4d60de359e72/1

#User function Template for python3

from collections import deque


class Solution:
    def shortestXYDist(self, grid, N, M):
        # code here
        vis = [[-1]*M for i in range(N)]
        q = deque()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "X":
                    q.append(([i, j], 0))
                    vis[i][j] = 1
        while q:
            coord, step = q.popleft()
            r = coord[0]
            c = coord[1]
            if grid[r][c] == "Y":
                return step
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            for i in range(4):
                nr = r+dr[i]
                nc = c+dc[i]
                if nr >= 0 and nr < N and nc >= 0 and nc < M and vis[nr][nc] != 1:
                    q.append(([nr, nc], step+1))
                    vis[nr][nc] = 1
        return -1


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().split())
        grid = []
        for i in range(N):
            ch = list(map(str, input().split()))
            grid.append(ch)

        ob = Solution()
        print(ob.shortestXYDist(grid, N, M))
# } Driver Code Ends
