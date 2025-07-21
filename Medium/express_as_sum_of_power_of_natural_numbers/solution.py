# Problem Statement: https://practice.geeksforgeeks.org/problems/express-as-sum-of-power-of-natural-numbers5647/1

# User function Template for python3
MODULO = 10**9 + 7


class Solution:
    def numOfWays(self, n, x):
        x_powers = []
        i, nx = 1, 1
        while nx <= n:
            x_powers.append(nx)
            i += 1
            nx = i**x
        dp = [0] * (n + 1)
        for nx in x_powers:
            for i in range(n - nx, 0, -1):
                if dp[i] == 0:
                    continue
                inx = i + nx
                dp[inx] = (dp[inx] + dp[i]) % MODULO
            dp[nx] = (dp[nx] + 1) % MODULO
        return dp[n]


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, x = input().split()
        n = int(n)
        x = int(x)
        ob = Solution()
        print(ob.numOfWays(n, x))

# } Driver Code Ends
