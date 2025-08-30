# Problem Statement: https://www.geeksforgeeks.org/problems/the-celebrity-problem/1

class Solution:
    def celebrity(self, mat):
        n=len(mat)
        a,b=0,n-1
        while a<b:
            if mat[a][b]:
                a+=1
            else:
                b-=1
        for i in range(n):
            if a!=i and mat[a][i] or not mat[i][a]:
                return -1
        return a