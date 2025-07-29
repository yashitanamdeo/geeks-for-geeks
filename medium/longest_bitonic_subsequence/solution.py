# Problem Statement: https://practice.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1

#User function Template for python3

class Solution:
	def LongestBitonicSequence(self, nums):
	    
	    n = len(nums)
	    left, right = [0]*n, [0]*n
	    
	    for i in range(n):
	        left[i] = 1
	        for j in range(i):
	            if nums[i] > nums[j]:
	                left[i] = max(left[i], left[j]+1)
	    for i in range(n-1, -1, -1):
	        right[i] = 1
	        for j in range(i+1, n):
	            if nums[i] > nums[j]:
	                right[i] = max(right[i], right[j]+1)
	                
	    ans = 0
	    for i in range(n):
	        ans = max(ans, left[i]+right[i]-1)
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.LongestBitonicSequence(nums)
		print(ans)
# } Driver Code Ends