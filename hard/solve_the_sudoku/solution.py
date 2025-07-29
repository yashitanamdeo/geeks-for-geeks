# Problem Statement: https://practice.geeksforgeeks.org/problems/solve-the-sudoku-1587115621/1

#User function Template for python3

class Solution:
    def is_safe_to_place(self, grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
                
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[i + start_row][j + start_col] == num:
                    return False
        return True
    
    def SolveSudoku(self, grid):
        empty_cell = self.find_empty_cell(grid)
        if not empty_cell:
            return True
            
        row, col = empty_cell
        
        for num in range(1, 10):
            if self.is_safe_to_place(grid, row, col, num):
                grid[row][col] = num
                
                if self.SolveSudoku(grid):
                    return True
                    
                grid[row][col] = 0
                
        return False
        
    def find_empty_cell(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return i, j
        return None
        
    def printGrid(self, arr):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end=" ")
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends