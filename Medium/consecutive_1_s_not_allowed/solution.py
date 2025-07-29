# Problem Statement: https://www.geeksforgeeks.org/problems/consecutive-1s-not-allowed1912/1

#User function Template for python3
class Solution:
    def countStrings(self, n):
        # Modulo constant for result
        modulo = 10**9 + 7

        # Initial values for Fibonacci sequence
        fib_prev, fib_current = 1, 2

        # Calculate Fibonacci sequence iteratively
        for i in range(2, n + 1):
            fib_prev, fib_current = fib_current, (fib_prev + fib_current) % modulo

        # Return the result for the given length n
        return fib_current


#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends