# Problem Statement: https://www.geeksforgeeks.org/problems/print-matrix-in-diagonal-pattern/1

# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        
        x,y = 0,0
        n = len(mat)
        ans = []
        add_x,add_y = -1,1
        while 0<=x<n and 0<=y<n:
            
            
            ans.append(mat[x][y])
            while 0<= x+add_x <n and 0<= y+add_y <n:
                
                x += add_x
                y += add_y
                ans.append(mat[x][y])
                
            if (x ==0 or x==n-1 ) and ( 0<=y<(n-1)):
                y += 1
            else:
                x += 1
            
            add_x,add_y = add_y,add_x
            
            
            
        return ans


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends