# Problem Statement: https://practice.geeksforgeeks.org/problems/lucky-numbers2911/1

#User function Template for python3

import math
class Solution:
    def isLucky(self, n): 
        #RETURN True OR False
        i=2
        while i<=n:
            if n%i==0:
                return 0
            n-=n//i  
            i+=1
        return 1  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        obj = Solution()
        if obj.isLucky(n):
            print(1)
        else:
            print(0)
        
# } Driver Code Ends