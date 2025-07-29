# Problem Statement: https://www.geeksforgeeks.org/problems/power-set4302/1

#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		res = []
		
		def solve(st, i):
		    if i == len(s):
		        return
		    
		    res.append(st+s[i])
		    
		    solve(st+s[i], i+1)
		    solve(st, i+1)
	    
	    solve("", 0)
	    return sorted(res)

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends