# Problem Statement: https://www.geeksforgeeks.org/problems/print-matrix-in-snake-pattern-1587115621/1


#User function Template for python3

class Solution:
    def snakePattern(self, matrix):
        row_position, result = 0, []
        for row in matrix:
            if row_position % 2:
                result += row[::-1]
            else:
                result += row
            row_position += 1
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.snakePattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends