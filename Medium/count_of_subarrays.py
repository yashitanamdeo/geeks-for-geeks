# Problem Statement: https://practice.geeksforgeeks.org/problems/count-of-subarrays5922/1

#User function Template for python3
class Solution:
	def countSubarray(self,arr, n, k):
	    # code here
	    res,cur=0,0
	    for i in range(n):
	        if arr[i]<=k:
	            cur+=1
	            res+=cur
	        else:
	            cur=0
	    return n*(n+1)//2-res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, k=map(int, input().strip().split())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.countSubarray(arr, n, k)
        print(ans)
        tc=tc-1
# } Driver Code Ends