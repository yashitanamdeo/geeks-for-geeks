# Problem Statement: https://practice.geeksforgeeks.org/problems/find-prime-numbers-in-a-range4718/1#

#User function Template for python3

class Solution:
    def isPrime(self,N):
        if N==1:
            return False
        for i in range(2,(int)(math.sqrt(N)+1)):
            if N%i==0:
                return False
        return True
    def primeRange(self,M,N):
        #code here
        v=[]
        for i in range(M,N+1):
            if self.isPrime(i):
                v.append(i)
        return v

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends