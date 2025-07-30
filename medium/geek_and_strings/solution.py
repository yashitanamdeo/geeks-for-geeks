# Problem Statement: https://practice.geeksforgeeks.org/problems/geek-and-strings3030/1

# User function Template for Python3

class Solution:

    def prefixCount(self, N, Q, li, query):
        # code here
        d = {}
        for i in li:
            s = ""
            for j in i[0]:
                s += j
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1
        m = []
        for i in query:
            if i[0] in d:
                m.append(d[i[0]])
            else:
                m.append(0)
        return m


# {
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        li = []
        for i in range(N):
            li.append(input().split())
        Q = int(input())
        query = []
        for i in range(Q):
            query.append(input().split())

        ob = Solution()
        ans = ob.prefixCount(N, Q, li, query)
        for i in range(Q):
            print(ans[i])
# } Driver Code Ends
