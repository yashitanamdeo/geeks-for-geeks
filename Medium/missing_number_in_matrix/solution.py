# Problem Statement: https://practice.geeksforgeeks.org/problems/missing-number-in-matrix5316/1

#User function Template for python3

class Solution:
	def MissingNo(self, matrix):
		n = len(matrix)
		x_0, y_0 = 0, 0
		
		row_red = [0] * n
		col_red = [0] * n
		
		left_diag_red = 0
		right_diag_red = 0
		
		for i, row in enumerate(matrix) :
		    left_diag_red += row[i]
		    right_diag_red += row[n - i - 1]
		    
		    for j, ele in enumerate(row) :
		        if not ele:
		            x_0 = i
		            y_0 = j
		        
		        row_red[i] += ele
		        col_red[j] += ele
	    
	    col_req_sum = col_red[y_0 - 1] if y_0 else col_red[y_0 + 1]
	    row_req_sum = row_red[x_0 - 1] if x_0 else row_red[x_0 + 1]
	    diff = col_req_sum - col_red[y_0]
	    
	    if diff <= 0 or diff != row_req_sum - row_red[x_0]:
	        return -1
	    
	    if x_0 == y_0 :
	        left_diag_red += diff
	    
	    if x_0 == (n - y_0 - 1):
	        right_diag_red += diff
	    
	    if left_diag_red != right_diag_red:
	        return -1
	    
	    row_red[x_0] += diff
	    col_red[y_0] += diff
	    
	    for num in row_red:
	        if num != left_diag_red:
	            return -1
	    
	    for num in col_red:
	        if num != right_diag_red:
	            return -1
	            
	   
	    return diff


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ans = ob.MissingNo(matrix)
		print(ans)

# } Driver Code Ends