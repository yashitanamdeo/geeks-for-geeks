# Problem Statement: https://www.geeksforgeeks.org/problems/reach-the-nth-point5433/1

#User function Template for python3

class Solution:
	def nthPoint(self,n):
		# Code here
		mod=10**9+7
		if n==0:
		    return 0
		one=1
		two=2
		res=0
		l=[]
		l.append(0)
		l.append(one)
		l.append(two)
		res=0
		for _ in range(3,n+1):
		    res=(one+two)%mod
		    one=two
		    two=res
		    l.append(res)
		return (l[n]%mod)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthPoint(n)
		print(ans)
# } Driver Code Ends
