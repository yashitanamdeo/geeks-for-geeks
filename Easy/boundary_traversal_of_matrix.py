# Problem Statement: https://practice.geeksforgeeks.org/problems/boundary-traversal-of-matrix-1587115620/1

#User function Template for python3

class Solution:
    
    #Function to return list of integers that form the boundary 
    #traversal of the matrix in a clockwise manner.
    def BoundaryTraversal(self,matrix, n, m):
        ans=[]
        row,col=0,0
        incr=1
        for _ in range(2):
            while True:
                if col==-1 or col==m:
                    col-=incr
                    row+=incr
                    if row==n:
                        return ans
                    break
                ans.append(matrix[row][col])
                col+=incr
            while True:
                if row==0 or row==n:
                    row-=incr
                    col-=incr
                    if col==-1:
                        return ans
                    break
                ans.append(matrix[row][col])
                row+=incr
            incr=-1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(m):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.BoundaryTraversal(matrix,n,m)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends