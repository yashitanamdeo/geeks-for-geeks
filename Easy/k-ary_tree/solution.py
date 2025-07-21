# Problem Statement: https://practice.geeksforgeeks.org/problems/k-ary-tree1235/1#


class Solution:
   def karyTree(self, k, m):
       # code here
    
      return pow(k,m,1000000007)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        k,m=map(int,input().split())
        
        ob = Solution()
        print(ob.karyTree(k,m))
# } Driver Code Ends