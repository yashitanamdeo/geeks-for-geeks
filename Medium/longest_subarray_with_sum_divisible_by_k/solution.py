# Problem Statement: https://www.geeksforgeeks.org/problems/longest-subarray-with-sum-divisible-by-k1259/1

# User function Template for python3
class Solution:
	def longSubarrWthSumDivByK(self, arr,  n, k):
		# Complete the function
		total, ans = 0, 0
		mp = dict()

		for i in range(n):
		    total += arr[i]
		    rem = total % k

		    if rem == 0:
		    	ans = max(ans, i+1)
		    if rem not in mp:
		        mp[rem] = i
		    else:
		        ans = max(ans, i - mp[rem])

		return ans


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':

	for _ in range(0, int(input())):
		n, K = map(int, input().split())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)


# } Driver Code Ends
