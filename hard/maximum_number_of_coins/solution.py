# Problem Statement: https://practice.geeksforgeeks.org/problems/7ae455e552dc4e07f76bbe2adc4d4207ce1ff16e/1

#User function Template for python3

class Solution():
    def maxCoins(self, N, a):
        dp = [[0]*N for _ in range(N)]

        for left in range(N, -1, -1):
            for right in range(left, N):
                for k in range(left, right+1):
                    v = a[k]
                    if left-1 >= 0:
                        v *= a[left-1]
                    if right+1 < N:
                        v *= a[right+1]
                    if left <= k-1:
                        v += dp[left][k-1]
                    if k+1 <= right:
                        v += dp[k+1][right]
                    dp[left][right] = max(dp[left][right], v)

        return dp[0][N-1]


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(Solution().maxCoins(n, a))
# } Driver Code Ends
