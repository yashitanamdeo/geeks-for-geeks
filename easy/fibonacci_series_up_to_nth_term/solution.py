# Problem Statement: https://www.geeksforgeeks.org/problems/fibonacci-series-up-to-nth-term/1

#User function Template for python3

class Solution:
    def series(self, n):
        # Code here
        a = 0
        b =1 
        fibo = []
        fibo.append(a)
        fibo.append(b)
        for i in range(0,n-1):
            c = fibo[i]+fibo[i+1]
            fibo.append(c%(10**9+7))
            
        return fibo 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends