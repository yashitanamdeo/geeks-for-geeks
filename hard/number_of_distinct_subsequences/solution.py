# Problem Statement: https://practice.geeksforgeeks.org/problems/number-of-distinct-subsequences0909/1

# User function Template for python3

class Solution:
    def distinctSubsequences(self, s):
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        last_occurrence = [-1] * 256

        for i in range(1, n + 1):
            char = s[i - 1]
            dp[i] = dp[i - 1] * 2 % 1000000007

            if last_occurrence[ord(char)] != -1:
                idx = last_occurrence[ord(char)]
                dp[i] -= dp[idx - 1] % 1000000007

            last_occurrence[ord(char)] = i

        return dp[n] % 1000000007


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.distinctSubsequences(s)
        print(answer)

# } Driver Code Ends
