# Problem Statement: https://www.geeksforgeeks.org/problems/brackets-in-matrix-chain-multiplication1024/1

#User function Template for python3

class Solution:
    def matrixChainOrder(self, p, n):
        n = len(p) - 1
        m = [[float('inf')] * n for _ in range(n)]
        s = [[''] * n for _ in range(n)]

        for i in range(n):
            m[i][i] = 0

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                    if q < m[i][j]:
                        m[i][j] = q
                        s[i][j] = k + 1

        result = self.construct_parenthesis(s, 0, n - 1)
        return result

    def construct_parenthesis(self, s, i, j):
        if i == j:
            return chr(ord('A') + i)
        else:
            left = self.construct_parenthesis(s, i, s[i][j] - 1)
            right = self.construct_parenthesis(s, s[i][j], j)
            return '(' + left + right + ')'


#{ 
 # Driver Code Starts

def get(p, n):
    m = [[0] * n for _ in range(n)]
    for i in range(1, n):
        m[i][i] = 0

    for L in range(2, n):
        for i in range(1, n - L + 1):
            m[i][i + L - 1] = float('inf')
            for k in range(i, i + L - 1):
                q = m[i][k] + m[k + 1][i + L - 1] + p[i - 1] * p[k] * p[i + L - 1]
                if q < m[i][i + L - 1]:
                    m[i][i + L - 1] = q

    return m[1][n - 1]

def find(s, p):
    arr = []
    ans = 0
    for t in s:
        if t == '(':
            arr.append((-1, -1))
        elif t == ')':
            b = arr.pop()
            a = arr.pop()
            arr.pop()
            arr.append((a[0], b[1]))
            ans += a[0] * a[1] * b[1]
        else:
            arr.append((p[ord(t) - ord('A')], p[ord(t) - ord('A') + 1]))

    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    ob = Solution()
    result = ob.matrixChainOrder(p, n)
    
    if find(result, p) == get(p, n):
        print("True")
    else:
        print("False")

# } Driver Code Ends
