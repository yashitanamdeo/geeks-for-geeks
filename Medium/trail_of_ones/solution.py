# Problem Statement: https://www.geeksforgeeks.org/problems/trail-of-ones3242/1

#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        fib = [0,1]
        mod = 10**9+7
        for i in range(2,n):
            fib.append((fib[i-1]+fib[i-2])%mod)

        ans = [0,1]
        for i in range(2,n):
            ans.append((ans[-1]*2 + fib[i])%mod)

        return ans[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends