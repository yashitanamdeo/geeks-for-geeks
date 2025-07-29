# Problem Statement: https://practice.geeksforgeeks.org/problems/set-bits0143/1

#User function Template for python3
class Solution:
	def setBits(self, N):
		n=bin(N) #convert it to a binary number string
		c=0 #set count to zero
		for i in n:
		    if i=='1':
		        c+=1
		return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.setBits(N)
		print(ans)




# } Driver Code Ends