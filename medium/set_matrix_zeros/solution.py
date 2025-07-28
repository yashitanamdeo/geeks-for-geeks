# Problem Statement: https://www.geeksforgeeks.org/problems/set-matrix-zeroes/1

class Solution:
    def setMatrixZeroes(self, mat):
        n, m = len(mat), len(mat[0])
        
        firstRow = firstCol = False
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    if i == 0:
                        firstRow = True
                    if j == 0:
                        firstCol = True
                    mat[i][0] = mat[0][j] = 0
                    
                    
        for i in range(1, n):
            for j in range(1, m):
                if mat[i][0]  == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
                    
        if firstRow:
            for j in range(m):
                mat[0][j] = 0
        
        if firstCol:
            for i in range(n):
                mat[i][0] = 0
        
        return mat