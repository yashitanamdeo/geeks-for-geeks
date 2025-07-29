# Problem Statement: https://www.geeksforgeeks.org/problems/sum-of-upper-and-lower-triangles-1587115621/1


#User function Template for python3


class Solution:
   
    def sumTriangles(self, matrix, matrix_size):
        # Initialize variables for the upper and lower triangles sums
        lower_triangle_sum, upper_triangle_sum = 0, 0
       
        # Loop through the rows and columns of the matrix
        for row in range(matrix_size):
            for col in range(matrix_size):
                # If the current row index is less than or equal to the current column index,
                # add the element to the lower triangle sum
                if row <= col:
                    lower_triangle_sum += matrix[row][col]
               
                # If the current row index is greater than or equal to the current column index,
                # add the element to the upper triangle sum
                if row >= col:
                    upper_triangle_sum += matrix[row][col]
       
        # Return the sums of the upper and lower triangles
        return lower_triangle_sum, upper_triangle_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]

        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        ans = obj.sumTriangles(matrix, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends