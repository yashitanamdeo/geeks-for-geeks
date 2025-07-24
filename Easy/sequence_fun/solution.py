# Problem Statement: https://practice.geeksforgeeks.org/problems/sequence-fun5018/1

#User function Template for python3

class Solution:
	def NthTerm(self, n):
	    r = 2
	    if r == 1:
	        return r

	    for i in range(2, n+1):
	        r = r*i+1

	    return r % (10**9+7)


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T = int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.NthTerm(n)
		print(ans)

# } Driver Code Ends
