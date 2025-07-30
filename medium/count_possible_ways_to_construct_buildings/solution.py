# Problem Statement: https://www.geeksforgeeks.org/problems/count-possible-ways-to-construct-buildings5007/1

#User function Template for python3

class Solution:
	def TotalWays(self, N):
		b= s = 1
		res = 0
		mod = 1000000007
		for i in range(N):
		    res = (b%mod+s%mod)%mod
		    b = s%mod
		    s = res%mod
	    return (res*res)%mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends