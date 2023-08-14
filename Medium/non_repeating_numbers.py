# Problem Statement: https://practice.geeksforgeeks.org/problems/finding-the-numbers0215/1

#User function Template for python3

class Solution:
    def singleNumber(self, nums):
    	xor=0
    	for e in nums:
    	    xor^=e
    	r=xor&(~(xor-1))
    	a,b=0,0
    	for e in nums:
    	    if r&e:
    	        a^=e
    	    else:
    	        b^=e
    	return sorted([b,a])



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends