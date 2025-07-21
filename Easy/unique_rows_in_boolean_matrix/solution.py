# Problem Statement: https://practice.geeksforgeeks.org/problems/unique-rows-in-boolean-matrix/1

#User function Template for python3

from typing import List


class Solution:
    def uniqueRow(self,row, col, matrix):
        l=[]
        for i in range(row):
            r=tuple(matrix[i])
            if r not in l: l.append(r)
        return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    testcase = int(input())
    while(testcase):
        s = input().split()
        row = int(s[0])
        col = int(s[1])
        matrix = [[None for _ in range(col)]for _ in range(row)]
        s = input().split()
        for i in range(row):
            for j in range(col):
                matrix[i][j] = int(s[i*col+j])
        
        ob = Solution()
        a = ob.uniqueRow(row, col, matrix)
        
        for row in a:
            for value in row:
                print(value,end = " ")
            print("$",end = "")
        print()
        testcase -= 1

if __name__ == "__main__":
    main()
# } Driver Code Ends