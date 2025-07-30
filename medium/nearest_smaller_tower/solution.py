# Problem Statement: https://practice.geeksforgeeks.org/problems/a520c08a8ea9b617be25c38b0fc2fe057e889253/1

#User function Template for python3

class Solution:
    def nearestSmallestTower(self, A):
        def _pre(r, out):
            stk = [(A[r.start], r.start)]
            for i in r[1:]:
                v = A[i]
                while stk and stk[-1][0] >= v:
                    stk.pop()
                out[i] = INV if not stk else stk[-1][1]
                stk.append((v, i))

        N, INV = len(A), 10**9
        LL, LR = [INV]*N, [INV]*N
        ans = [-1] * N
        _pre(range(N), LL)
        _pre(range(N-1, -1, -1), LR)
        for i in range(N):
            if LL[i] == LR[i] == INV:
                continue
            Ldif, Rdif = abs(i-LL[i]), abs(LR[i]-i)
            if Ldif < Rdif:
                ans[i] = LL[i]
            elif Ldif > Rdif:
                ans[i] = LR[i]
            elif A[LL[i]] <= A[LR[i]]:
                ans[i] = LL[i]
            else:
                ans[i] = LR[i]
        return ans


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        N = int(input())
        arr = [int(i) for i in input().strip().split()]
        obj = Solution()
        ans = obj.nearestSmallestTower(arr)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends
