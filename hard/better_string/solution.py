# Problem Statement: https://www.geeksforgeeks.org/problems/better-string/1

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

class Solution:
    def count_distinct_subsequences(self, s):
        length = len(s)
        modulo = 10**9 + 7
        dp = [0] * (length + 1)
        dp[0] = 1
        last_occurrence_index = {}

        for i in range(1, length + 1):
            dp[i] = (2 * dp[i - 1]) % modulo
            if s[i - 1] in last_occurrence_index:
                dp[i] -= dp[last_occurrence_index[s[i - 1]] - 1]
            last_occurrence_index[s[i - 1]] = i

        return dp[length]

    def betterString(self, str1, str2):
        if self.count_distinct_subsequences(str1) >= self.count_distinct_subsequences(str2):
            return str1
        else:
            return str2


# {
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends
