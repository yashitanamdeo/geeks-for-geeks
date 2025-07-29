# Problem Statement: https://practice.geeksforgeeks.org/problems/replace-os-with-xs0052/1

# User function Template for python3

class Solution:
    def dfs(self, v, mat, x, y, n, m):
        t = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        v[x][y] = 1
        for i in t:
            x1, y1 = i[0]+x, i[1]+y
            if (x1 >= 0 and x1 < n) and (y1 >= 0 and y1 < m) and v[x1][y1] != 1 and mat[x1][y1] != 'X':
                self.dfs(v, mat, x1, y1, n, m)

        return v

    def fill(self, n, m, mat):
        # code here
        visited = [[0 for j in range(m)] for i in range(n)]

        for i in range(m):
            if mat[0][i] == 'O' and visited[0][i] == 0:
                visited = self.dfs(visited, mat, 0, i, n, m)
        for i in range(n):
            if mat[i][0] == 'O' and visited[i][0] == 0:
                visited = self.dfs(visited, mat, i, 0, n, m)
        for i in range(m):
            if mat[n-1][i] == 'O' and visited[n-1][i] == 0:
                visited = self.dfs(visited, mat, n-1, i, n, m)
        for i in range(n):
            if mat[i][m-1] == 'O' and visited[i][m-1] == 0:
                visited = self.dfs(visited, mat, i, m-1, n, m)

        return [['O' if visited[i][j] == 1 else 'X' for j in range(m)] for i in range(n)]


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str, input().split()))
            mat.append(s)

        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()
# } Driver Code Ends
