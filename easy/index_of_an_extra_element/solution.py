# Problem Statement: https://www.geeksforgeeks.org/problems/index-of-an-extra-element/1

class Solution:
    def findExtra(self,n,a,b):
        l,h=0,n-1
        while l<=h:
            mid=(l+h)//2
            if mid>0 and a[mid]==b[mid-1]:
                h=mid-1
            elif mid<n-1 and a[mid]==b[mid]:
                l=mid+1
            else:
                return mid


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(Solution().findExtra(n, a, b))

# } Driver Code Ends