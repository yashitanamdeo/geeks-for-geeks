# Problem Statement: https://www.geeksforgeeks.org/problems/determinant-of-a-matrix-1587115620/1


# User function Template for python3

class Solution:

    def determinantOfMatrix(self, matrix, n):
        if n == 1:
            return matrix[0][0]
        if n == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        else:
            det = 0
            for i in range(n):
                if i % 2 == 0:
                    flag = 1
                else:
                    flag = -1
                mat = [row[0:i] + row[i+1:] for row in matrix[1:]]
                det += flag*matrix[0][i]*self.determinantOfMatrix(mat, n-1)
            return det


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(values[k])
                k += 1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix, n))
# } Driver Code Ends
