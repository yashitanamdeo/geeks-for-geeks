# Problem Statement: https://practice.geeksforgeeks.org/problems/magic-triplets4003/1

#User function Template for python3

class Solution:
	def countTriplets(self, nums):
	    count = 0
	    for i in range(1, len(nums)):
	        left, right = 0, 0
	        for j in range(i-1, -1, -1):
	            if nums[j] < nums[i]:
	                left += 1
	        for j in range(i+1, len(nums)):
	            if nums[j] > nums[i]:
	                right += 1
	        count += (left*right)
	    return count


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T = int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.countTriplets(nums)
		print(ans)

# } Driver Code Ends
