# Problem Statement: https://practice.geeksforgeeks.org/problems/nth-fibonacci-number1335/1

class Solution:

    def nthFibonacci(self, n: int) -> int:

        MOD = 1000000007

        if n == 0:
            return 0
        elif n == 1:
            return 1

        dp = [0]*(n+1)

        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD

        return dp[n]


# {
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.nthFibonacci(n)

        print(res)


# } Driver Code Ends
