#  Problem Statement: https://practice.geeksforgeeks.org/problems/find-first-set-bit-1587115620/1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        ans=1
        if n==0:
            return 0
        while n>0:
            res = n & 1
            if res==1:
                return ans
            ans+=1
            n = n>>1
        return 0
        

#{ 
 # Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends