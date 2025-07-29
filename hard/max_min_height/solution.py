# Problem Statement: https://practice.geeksforgeeks.org/problems/899540d741547e2d75d1c5c03a4161ab53affd13/1

#User function Template for python3

class Solution():
    def maximizeMinHeight(self, n, k, w, a):
        def _try(tar):
            mods = [0]*n
            add, left = 0, k
            for i in range(n):
                add += mods[i]
                v = a[i] + add
                if v < tar:
                    Δ = tar-v
                    mods[i] += Δ
                    if i+w < n:
                        mods[i+w] -= Δ
                    add += Δ
                    left -= Δ
                    if left < 0:
                        return False
            return True

        L = min(a)
        R = L + k + 1
        while L < R:
            m = (L+R)//2
            if _try(m):
                L = m+1
            else:
                R = m
        return L-1

#{
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n, k, w = map(int, input().split())
    arr = [int(i) for i in input().split()]
    print(Solution().maximizeMinHeight(n, k, w, arr))

# } Driver Code Ends
