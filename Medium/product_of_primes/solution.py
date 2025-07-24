# Problem Statement: https://practice.geeksforgeeks.org/problems/product-of-primes5328/1#git

#User function Template for python3

import math
class Solution:
    def isprime(self,n):
        if n==1:
            return False
        if n==2 or n==3:
            return True
        if n%2==0 or n%3==0:
            return False
        for i in range(5,int(n**(0.5))+1,6):
            if n%i==0 or n%(i+2)==0:
                return False
        return True
    
    def primeProduct(self, L, R):
        # code here
        prime = 1
        for n in range(L,R+1):
            if self.isprime(n):
                prime*=n
        return(prime%(1000000007))


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, R = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.primeProduct(L, R))
# } Driver Code Ends