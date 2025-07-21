# Problem Statement: https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1

# User function Template for python3

class Solution:
    def longestPalin(self, S):
        n = len(S)
        start = 0
        maxLength = 1

        # Function to expand around the center
        def expandAroundCenter(left, right):
            nonlocal start, maxLength
            while left >= 0 and right < n and S[left] == S[right]:
                left -= 1
                right += 1
            length = right - left - 1
            if length > maxLength:
                maxLength = length
                start = left + 1

        for i in range(n):
            # Check for odd-length palindromes
            expandAroundCenter(i, i)

            # Check for even-length palindromes
            expandAroundCenter(i, i + 1)

        return S[start:start + maxLength]


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends
