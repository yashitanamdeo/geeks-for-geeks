# Problem Statement: https://www.geeksforgeeks.org/problems/print-n-bit-binary-numbers-having-more-1s-than-0s0252/1

#User function Template for python3
class Solution:     # line 1
	def NBitBinary(self, n):
		res = []
		
		def oneorzero(string, length, zeros):
		    if length == n:
		        res.append(string)
		        return
		    
		    oneorzero(string+'1', length+1, zeros)
		    
		    if (length-zeros) > zeros:
		        oneorzero(string+'0', length+1, zeros+1)
        
        oneorzero('1', 1, 0)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends