# Problem Statement: https://practice.geeksforgeeks.org/problems/transpose-of-matrix-1587115621/1

#User function Template for python3

class Solution:
    def transpose(self, matrix, n):
        # Write Your code here
        for i in range(0,n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        return matrix


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
        
    ob = Solution()
    ob.transpose(matrix, n)
    
    for row in matrix:
        print(*row)
    
# } Driver Code Ends