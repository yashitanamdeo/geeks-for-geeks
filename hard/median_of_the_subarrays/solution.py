# Problem Statement: https://practice.geeksforgeeks.org/problems/6f08220ca3b871be594f50f7f56a9ef2799cb485/1

#User function Template for python3
class Solution:
    def countSubarray(self, N, A, M):
        # code here
        def fn(n, A, m):
            mp = [0]*(2*n+1)
            cur, tot, ans = n, 0, 0
            mp[cur] += 1

            for i in range(n):
                x = -1
                if (A[i] >= m):
                    x = 1
                if (x == -1):
                    tot -= mp[(cur+x)]
                else:
                    tot += mp[cur]

                cur += x
                ans += tot
                mp[cur] += 1

            return ans

        return fn(N, A, M) - fn(N, A, M+1)


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countSubarray(N, A, M)
        print(ans)

# } Driver Code Ends
