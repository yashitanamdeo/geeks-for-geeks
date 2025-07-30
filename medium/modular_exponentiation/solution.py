# Problem Statement: https://www.geeksforgeeks.org/problems/modular-exponentiation-for-large-numbers5537/1

#User function Template for python3

class Solution:
    def PowMod(self, x, n, m):
        # Code here
        ans = 1
        while n > 0:
                if n & 1:
                    ans = (ans * x) % m
                x = (x*x) % m
                n = n // 2
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends