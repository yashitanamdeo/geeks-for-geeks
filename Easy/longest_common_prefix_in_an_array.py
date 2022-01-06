# Problem Statement: https://practice.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1

#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        i,fail,pfix=0,0,''
        while i<len(min(arr)):
            for j in range(1,n):
                #print(i,j,arr[0][i])
                if arr[0][i]!=arr[j][i]:
                    fail=1
                    break
            if fail==1: 
                break 
            else:
                pfix=pfix+arr[0][i]
                i+=1
        if len(pfix)==0: 
            return (-1)
        else: 
            return pfix
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends