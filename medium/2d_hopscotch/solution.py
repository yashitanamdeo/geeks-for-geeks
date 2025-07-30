# Problem Statement: https://practice.geeksforgeeks.org/problems/hopscotch4857/1

#User function Template for python3

class Solution:
    def hopscotch(self, n, m, mat, ty, i, j):
        i, j = 2*i + j%2, 2*j 
        res = 0
        
        if ty == 0:
            for di, dj in [[-2,0], [2,0], [-1,-2], [-1,2], [1,-2], [1,2]]:
                ni, nj = (i + di)//2, (j + dj)//2
                if 0 <= ni < n and 0 <= nj < m:
                    res += mat[ni][nj]
        else:
            for di, dj in [[-4,0], [4,0], [0,-4], [0,4], [-3,-2], [-3,2], [3,-2], [3,2], [-2,-4], [-2,4], [2,-4], [2,4]]:
                ni, nj = (i + di)//2, (j + dj)//2
                if 0 <= ni < n and 0 <= nj < m:
                    res += mat[ni][nj]
            
        return res

# 1. Map original space

# Scale coordinates by 2
# Shift down odd columns by 1
# 2. If ty = 0, find coordinates at distance 2 or 3 in mapped space. Else, find coordinates at distance 4, 5 or 6  in mapped space. 

# 3. Map these coordinates back to original space.

# 4. Obtain required sum of elments at these postions. 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = [[0]*m for x in range(n)]
        for i in range(n):
            arr = input().split()
            for j in range(m):
                mat[i][j] = int(arr[j])
        ty, i, j = map(int,input().strip().split())
        
        ob = Solution()
        print(ob.hopscotch(n, m, mat, ty, i, j))
# } Driver Code Ends