# Problem Statement: https://practice.geeksforgeeks.org/problems/rotate-by-90-degree0356/1#

#User function Template for python3

def rotate(matrix): 
   #code here
   mat = []
   N = len(matrix[0])
   mat = [[matrix[j][i] for j in range(N)]for i in range(N-1,-1,-1)]

   for i in range(N):
       matrix[i] = mat[i]
       
#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N=int(input())
		arr=[int(x) for x in input().split()]
		matrix=[]

		for i in range(0,N*N,N):
			matrix.append(arr[i:i+N])

		rotate(matrix)
		for i in range(N): 
			for j in range(N): 
				print(matrix[i][j], end =' ') 
			print() 
        

# } Driver Code Ends