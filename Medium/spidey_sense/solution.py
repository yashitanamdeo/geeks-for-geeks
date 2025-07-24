# Problem Statement: https://practice.geeksforgeeks.org/problems/spidey-sense5556/1

from collections import deque

class Solution:
    def findDistance(self, matrix, m, n):
        # Your code goes here
        # bfs 
        def issafe(ith,jth):
            if ith >= 0 and ith < len(matrix) and jth>=0 and jth < len(matrix[0])\
            and visited[ith][jth] == False and matrix[ith][jth] == "O":
                return True
            return False
        q = deque()
        visited = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'W':
                    matrix[i][j] = -1
                elif matrix[i][j] == 'B':
                    q.append([i,j])
        moves = [[0,1],[1,0],[-1,0],[0,-1]]
        level = -1
        while(q):
            size = len(q)
            level += 1
            while(size):
                ele = q.popleft()
                if matrix[ele[0]][ele[1]] == "O":
                    matrix[ele[0]][ele[1]] = level
                visited[ele[0]][ele[1]] = True
                if matrix[ele[0]][ele[1]] == 'B':
                    matrix[ele[0]][ele[1]] = 0
                for move in moves:
                    if issafe(ele[0]+move[0],ele[1]+move[1]):
                        q.append([ele[0]+move[0],ele[1]+move[1]])
                size-=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 'O':
                    matrix[i][j] = -1
        return matrix




#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        size = input().strip().split()
        m = int(size[0])
        n = int(size[1])
        matrix=[]
        for _ in range(m):
            matrix.append( [ x for x in input().strip().split() ] )
        obj = Solution() 
        result = obj.findDistance(matrix,m,n)
        for i in result:
            for j in i:
                print(j, end=' ')
            print()
# } Driver Code Ends