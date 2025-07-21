# Problem Statement: https://practice.geeksforgeeks.org/problems/maximum-index3307/1

#User function Template for python3
class Solution:

	def maxIndexDiff(self,arr,n):
        #code here
        for i in range(n):
            arr[i]=(i,arr[i])
            
        arr.sort(key=lambda x:x[1])
        
        diff=0
        far=float("-inf")
        for i in range(n-1,-1,-1):
            curr=arr[i][0]
            if curr>far:
                far=curr
            else:
                diff=max(diff,far-curr)
            
        return diff
    
    # Solution 2
    ''' 
    def maxIndexDiff(self,a, n): 
        l_min,r_max=[a[0]]*n,[a[-1]]*n
        for i in range(1,n):
            l_min[i]=min(l_min[i-1],a[i])
            r_max[-i-1]=max(r_max[-i],a[-i-1])
        l,r,ans=0,0,0
        while l<n and r<n:
            if l_min[l]<=r_max[r]:
                ans=max(ans,r-l)
                r+=1
            else:
                l+=1
        return ans
    '''


#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends