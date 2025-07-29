# Problem Statement: https://practice.geeksforgeeks.org/problems/reversing-the-equation2205/1

# User function Template for python3

class Solution:
    def __init__(self):
        self.ans = ""
        self.st = []

    def reverseEqn(self, s):
        start = 0
        for i in range(len(s)):
            sub_str = s[start:i]
            if not s[i].isdigit():
                self.st.append(sub_str)
                self.st.append(s[i])
                start = i + 1

        # Push remaining string elements to the stack
        self.st.append(s[start:])

        while self.st:
            self.ans += self.st.pop()

        return self.ans


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends
