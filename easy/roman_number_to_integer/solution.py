# Problem Statement: https://practice.geeksforgeeks.org/problems/roman-number-to-integer3201/1

# User function Template for python3

class Solution:
    def romanToDecimal(self, S):
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        n = len(S)
        ans = 0
        for i in range(n-1, -1, -1):
            if i == n-1 or roman[S[i]] >= roman[S[i+1]]:
                ans += roman[S[i]]
            else:
                ans -= roman[S[i]]
        return ans


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends
