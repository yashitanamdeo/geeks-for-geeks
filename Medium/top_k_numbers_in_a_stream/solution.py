# Problem Statement: https://www.geeksforgeeks.org/problems/top-k-numbers3425/1

# User function Template for python3

class Solution:
    def kTop(self, a, N, K):
        # code here.
        d = {}
        res = []
        for i in range(N):
            d[a[i]] = d.get(a[i], 0)+1
            q = sorted(d.items(), key=lambda x: (x[1], -x[0]), reverse=1)
            if len(q) < K:
                res.append([j for j, _ in q])
            else:
                res.append([j for j, _ in q[:K]])
        return res


# {
 # Driver Code Starts


t = int(input())
for _ in range(0, t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ob = Solution()
    ans = ob.kTop(a, n, k)
    for line in ans:
        print(*line)


# } Driver Code Ends
