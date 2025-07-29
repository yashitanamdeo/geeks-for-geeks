# Problem Statement: https://practice.geeksforgeeks.org/problems/palindrome-string0817/1

# User function Template for python3
class Solution:
    def isPalindrome(self, S):
        rev_S = S[::-1]
        if S == rev_S:
            return 1
        else:
            return 0

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.isPalindrome(S)
        print(answer)

# } Driver Code Ends
