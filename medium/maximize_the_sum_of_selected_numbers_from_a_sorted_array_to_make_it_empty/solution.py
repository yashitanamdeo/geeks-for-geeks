# Problem Statement: https://practice.geeksforgeeks.org/problems/maximize-the-sum-of-selected-numbers-from-an-array-to-make-it-empty0836/1

#User function Template for python3

class Solution:
    
    def maximizeSum (self,arr, n) : 
        #Complete the function
        m=[0]*(100001)
        for x in arr:
            m[x]+=1
        sumi=0
        for i in range(n-1,-1,-1):
            curr=arr[i]
            if m[curr]!=0:
                sumi+=curr
                m[curr]-=1
                if m[curr-1]!=0:
                    m[curr-1]-=1
        return sumi


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    ob=Solution()
    
    ans = ob.maximizeSum(arr, n)
    print(ans)

# } Driver Code Ends