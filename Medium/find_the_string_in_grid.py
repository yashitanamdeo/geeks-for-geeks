# Problem Statement: https://practice.geeksforgeeks.org/problems/find-the-string-in-grid0111/1

#User function Template for python3

class Solution:
    def explore(self, grid, word, x, y, dx, dy, n, m):
        for k in range(1, len(word)):
            cx = x + (k * dx)
            cy = y + (k * dy)
            
            if cx<0 or cx== n or cy < 0 or cy==m or grid[cx][cy]!=word[k]:
                return False
        return True
        
    def dfs(self, grid, word, x, y, n, m):
        directions = [[-1,0], [-1,-1], [0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1]]
        
        for dx, dy in directions:
            if self.explore(grid, word, x, y, dx, dy, n, m):
                return True
        return False
    
	def searchWord(self, grid, word):
		# Code here
		res = []
		n, m = len(grid), len(grid[0])
		
		for i in range(n):
		    for j in range(m):
		        if grid[i][j] == word[0]:
		            if self.dfs(grid, word, i, j, n, m):
		                res.append([i, j])

		return sorted(res)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends