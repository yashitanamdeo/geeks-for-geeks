# Problem Statement: https://practice.geeksforgeeks.org/problems/make-matrix-beautiful-1587115620/1

#User function Template for python3

class Solution:
    def findMinOpeartion(self, matrix, n):
        # Code here
        max_v = 0
        row = 0
        cur_s = 0
        for i in matrix:
            row += 1
            s = sum(i)
            max_v = max(s,max_v)
            cur_s += s
        for j in range(n):
            s = 0
            for i in range(n):
                s += matrix[i][j]
            max_v = max(s,max_v)
        ans = max_v*row - cur_s
        return ans


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    ob = Solution()
    print(ob.findMinOpeartion(matrix, n))
# } Driver Code Ends