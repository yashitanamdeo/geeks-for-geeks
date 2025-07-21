# Problem Statement: https://practice.geeksforgeeks.org/problems/maximum-product-of-increasing-subsequence-of-size-32027/1#

from bisect import bisect_left as bl
class Solution:
   
    def binPartition(self,a, value):
        return bl(a, value)-1
       


    def countArray (self, a, n) : 
        if n<3:
            return [-1]
        left=[-1,a[0]]
        result=[-1]
        right=max(a[1:])
        maxproduct=-1
        for i in range(1,n-1):
            current=a[i]
            if current>=right:
                right=max(a[i+1:])

            j=self.binPartition(left,current)
           
           
            leftValue=left[j]
            left.insert(j+1,current)
            rightValue=right
            
            if not(leftValue<current and current<rightValue):
                continue
            currentprod=leftValue*rightValue*current
            if currentprod>maxproduct:
                maxproduct=currentprod
                result=[leftValue,current,rightValue]
           
           
        return result


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ans = Solution().countArray(arr, n)
    if(ans[0] == -1):
        print("Not Present")
    else:
        print(*ans)
# } Driver Code Ends