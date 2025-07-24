# Problem Statement: https://practice.geeksforgeeks.org/problems/cutting-binary-string1342/1

# User function Template for python3

class Solution:

    def cuts(self, s):

        def ok(ss):
            n = int(ss, 2)
            while n > 1 and n % 5 == 0:
                n //= 5
            return n == 1

        n = len(s)
        dp = [float('inf')]*(n+1)
        dp[0] = 0

        for i in range(n):
            for k in range(i, -1, -1):
                if s[k] != '0' and ok(s[k:i+1]):
                    dp[i+1] = min(dp[i+1], dp[k]+1)
        return dp[n] if dp[n] != float('inf') else -1
    
    def cuts2(self, s: str) -> int:
        n = len(s)

        # Precompute powers of 5 up to length 30
        powers_of_5 = set()
        i = 0
        while True:
            power = 5 ** i
            binary = bin(power)[2:]
            if len(binary) > n:
                break
            powers_of_5.add(binary)
            i += 1

        # Initialize dp array
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # base case: empty string needs 0 cuts

        for i in range(1, n + 1):
            for j in range(i):
                substring = s[j:i]
                if substring[0] != '0' and substring in powers_of_5:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        print(solObj.cuts(s))

# } Driver Code Ends
