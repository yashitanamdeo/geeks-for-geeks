# Problem Statement: https://practice.geeksforgeeks.org/problems/santa-banta2814/1

# User function Template for python3

class Solution:
    def precompute(self):
        primes = [True]*(10**6)
        primes[0] = False
        primes[1] = False
        for i in range(len(primes)):
            if not primes[i]:
                continue
            for j in range(i*i, len(primes), i):
                primes[j] = False
        self.primes = [i for i, t in enumerate(primes) if t]

    def helpSanta(self, n, m, g):
        from collections import defaultdict
        if m == 0:
            return -1

        arr = [i for i in range(n+1)]

        def find(i):
            if arr[i] != i:
                arr[i] = find(arr[i])
            return arr[i]

        for i, grp in enumerate(g):
            if i > n:
                break

            rx = find(i)
            for y in grp:
                ry = find(y)
                if rx != ry:
                    arr[ry] = rx

        num = 0
        cnt = defaultdict(int)
        for i in range(1, n+1):
            r = find(i)
            cnt[r] += 1
            num = max(num, cnt[r])
        return self.primes[num-1]


# {
 # Driver Code Starts
# Initial Template for Python 3

ob = Solution()
ob.precompute()
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n+10)]
    for i in range(m):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)
    ans = ob.helpSanta(n, m, arr)
    print(ans)
# } Driver Code Ends
