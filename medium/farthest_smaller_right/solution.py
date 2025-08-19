# Problem Statement: https://www.geeksforgeeks.org/problems/farthest-smaller-right/1

class Solution:
    def bs(self,arr,l,h,x):
        while l<=h:
            mid=(l+h)//2
            if arr[mid]>=x:
                h=mid-1
            else:
                l=mid+1
        return l-1
    
    def farMin(self, arr):
        n=len(arr)
        right=[0]*n
        right[n-1]=arr[n-1]
        for i in range(n-2,-1,-1):
            right[i]=min(arr[i],right[i+1])
        ans=[None]*n
        for i in range(n):
            if i==n-1 or right[i+1]>=arr[i]:
                ans[i]=-1
            else:
                ans[i]=self.bs(right,i+1,n-1,arr[i])
        return ans