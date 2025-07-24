# Problem Statement: https://practice.geeksforgeeks.org/problems/253524a82f7b4561dc33ff637cd3b92c33d4f216/1

#User function Template for python3

class Solution:    
    def ValidCorner(self,matrix): 
        n,m=len(matrix),len(matrix[0])
        for i in range(n):
            if matrix[i].count(1)>1:
                s=set()
                for k in range(m):
                    if matrix[i][k]==1:s.add(k)
                for j in range(i+1,n):
                    if matrix[j].count(1)>1:
                        cnt=0
                        for p in range(m):
                            if matrix[j][p]==1 and p in s and cnt<2:cnt+=1
                        if cnt==2:return True
                        cnt=0
                       
        return False

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		r = int(input())
		c = int(input())
		line = input().strip().split()
		mat = [ [0 for _ in range(c)] for _ in range(r) ]
		for i in range(r):
			for j in range(c):
				mat[i][j] = int( line[i*c+j] )
		ob=Solution()
		if (ob.ValidCorner(mat)): 
			print("Yes") 
		else: 
			print("No") 


# } Driver Code Ends