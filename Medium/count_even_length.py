# Problem Statement: https://practice.geeksforgeeks.org/problems/count-even-length1907/1

#User function Template for python3

import math
mod = 10**9+7

class Solution:
    
    def compute_value(self, n):
        a=math.factorial(2*n)
        b=math.factorial(n)

        return (a//(b**2))%mod




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.compute_value(n)
		print(ans)
# } Driver Code Ends