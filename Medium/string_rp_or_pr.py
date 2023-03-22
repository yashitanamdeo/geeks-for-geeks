# Problem Statement: https://practice.geeksforgeeks.org/problems/d25f415de2ff3e02134de03e17ad019d723ab2e9/1

#User function Template for python3

class Solution:
    def solve(self, X, Y, S):

        def rp(string, x, y, ans, flag):
            stack = []
            for char in string:
                if char == 'p':
                    if stack and stack[-1] == 'r':
                        ans[0] += y
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
            if flag:
                pr("".join(stack), x, y, ans, False)

        def pr(string, x, y, ans, flag):
            stack = []
            for char in string:
                if char == 'r':
                    if stack and stack[-1] == 'p':
                        ans[0] += x
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
            if flag:
                rp("".join(stack), x, y, ans, False)
        ans = [0]
        if X > Y:
            pr(S, X, Y, ans, True)
        else:
            rp(S, X, Y, ans, True)
        return ans[0]


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str = input().split()
        X = int(str[0])
        Y = int(str[1])
        S = input()

        ob = Solution()
        print(ob.solve(X, Y, S))
# } Driver Code Ends
