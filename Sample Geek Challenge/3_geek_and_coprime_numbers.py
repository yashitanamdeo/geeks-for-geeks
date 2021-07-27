#User function Template for python3
import math

class Solution:
        
    def sum(self, N, M):
        num = math.gcd(N,M) #to find the highest common factor
        quotient1 = N//num
        quotient2 = M//num
        return(quotient1+quotient2)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N,M = map(int,input().strip().split())

        ob = Solution()
        print(ob.sum(N, M))

# } Driver Code Ends