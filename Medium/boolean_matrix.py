# Problem Statement: https://practice.geeksforgeeks.org/problems/boolean-matrix-problem-1587115620/1

# User function Template for python3


# Function to modify the matrix such that if a matrix cell matrix[i][j]
# is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])
    d = {"row": set(), "col": set()}
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                d["row"].add(i)
                d["col"].add(j)
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0 and ((i in d["row"]) or (j in d["col"])):
                matrix[i][j] = 1


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()


# } Driver Code Ends
