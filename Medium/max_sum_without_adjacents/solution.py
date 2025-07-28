# Problem Statement: https://www.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1

#User function Template for python3
class Solution:
	
    def findMaxSum(self,arr, n):
        if(n==1):
            return arr[0]
        if(n>2):
            arr[n-3]=arr[n-3]+arr[n-1]
            i = n - 4
            while(i>=0):
                arr[i]= arr[i]+max(arr[i+2],arr[i+3])
                i -= 1
        return max(arr[0],arr[1]);


class Solution2:

	def findMaxSum(self, arr, n):
		# code here
		res, pre, cur = 0, 0, 0
		for i in range(n):
		    cur = pre + arr[i]
		    pre = res
		    res = max(cur, res)
		return res
     
#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends