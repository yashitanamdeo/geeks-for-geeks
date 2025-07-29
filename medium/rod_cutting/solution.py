# Problem Statement: https://practice.geeksforgeeks.org/problems/rod-cutting0840/1

# User function Template for python3

class Solution:
    def cutRod(self, price, n):
        dp = [0] * (n+1)

        for i in range(1, n+1):
            dp[i] = price[i-1]
            for num in range(1, i+1):
                dp[i] = max(dp[i], dp[num]+dp[i-num])
        return dp[-1]


# {
 # Driver Code Starts
# Initial Template for Python 3

def main():

    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
