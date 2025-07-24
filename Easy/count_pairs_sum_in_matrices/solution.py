# Problem Statement: https://www.geeksforgeeks.org/problems/count-pairs-sum-in-matrices4332/1

#User function Template for python3
class Solution:
	def countPairs(self, mat1, mat2, n, x):
		## i1 -> track elements of matrix mat1 from 0 to n-1
		## j1 -> track row of matrix mat1 from 0 to n-1
		## i2 -> track elements of matrix mat2 from n-1 to 0
		## j2 -> track row of matrix mat2 from n-1 to 0
		
		i1 = j1 = 0
		i2= j2 = n-1
		count = 0
		while j1 < n and j2 > -1:
		    ## Case 1: mat1[j1][i1] + mat2[j2][i2] == x
		    
		    ## next index in mat1, if greater than equal to n,
		    ## go to next row with 1st element
		    
		    ## previous index in mat2, if less than equal to -1,
		    ## go to previous row last element
		    if mat1[j1][i1] + mat2[j2][i2] == x:
		        count += 1
		        i1 += 1
		        if i1 >= n:
		            i1 = 0
		            j1 += 1
		        i2 -= 1
		        if i2 <= -1:
		            i2 = n-1
		            j2 -= 1
		    ## Case 2: mat1[j1][i1] + mat2[j2][i2] > x
		    ## previous index in mat2, if less than equal to -1,
		    ## go to previous row last element
		    elif mat1[j1][i1] + mat2[j2][i2] > x:
		        i2 -= 1
		        if i2 <= -1:
		            i2 = n-1
		            j2 -= 1
		    ## Case 3: mat1[j1][i1] + mat2[j2][i2] < x
		    ## next index in mat1, if greater than equal to n,
		    ## go to next row with 1st element
		    elif mat1[j1][i1] + mat2[j2][i2] < x:
		        i1 += 1
		        if i1 >= n:
		            i1 = 0
		            j1 += 1
        return count 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends