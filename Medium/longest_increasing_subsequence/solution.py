# Problem Statement: https://practice.geeksforgeeks.org/problems/longest-increasing-subsequence-1587115620/1

#User function Template for python3

class Solution:
    
    #Function to find length of longest increasing subsequence.
    def getUpInd(self, a, t, l, r, k):
 
        while (r - l > 1):
         
            m = l + (r - l)//2
            if (a[t[m]] >= k):
                r = m
            else:
                l = m
 
        return r
    
    def longestSubsequence(self,a,n):
        # code here
        tailIndices =[0 for i in range(n + 1)] 
 
        prevIndices =[-1 for i in range(n + 1)] 
         
    
        len = 1
        for i in range(1, n):
         
            if (a[i] < a[tailIndices[0]]):
             
                tailIndices[0] = i
             
            elif (a[i] > a[tailIndices[len-1]]):
             
 
                prevIndices[i] = tailIndices[len-1]
                tailIndices[len] = i
                len += 1
             
            else:
                pos = self.getUpInd(a, tailIndices, -1, len-1, a[i])
      
                prevIndices[i] = tailIndices[pos-1]
                tailIndices[pos] = i
             

      
        return len
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends