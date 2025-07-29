# Problem Statement: https://practice.geeksforgeeks.org/problems/return-two-prime-numbers2509/1#

#User function Template for python3

class Solution:
    def primeDivision(self, N):
        
        def isPrime(num):
            if num < 2:
                return False
            i = 2
            while(i*i <= num):
                if num%i == 0:
                    return False
                i += 1
            return True
        
        if N < 3:
            return(-1, -1)
        for i in range(2,(N//2)+1):
            if isPrime(i) and isPrime(N-i):
                return(i, N-i)
        return(-1,-1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends