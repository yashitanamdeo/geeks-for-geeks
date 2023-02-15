class Solution:
    def minCost(self, colors, N):
        a = [0] * N
        b = [0] * N
        c = [0] * N
        a[0] = colors[0][0]
        b[0] = colors[0][1]
        c[0] = colors[0][2]
        for i in range(1, N):
            a[i] = colors[i][0] + min(b[i-1], c[i-1])
            b[i] = colors[i][1] + min(a[i-1], c[i-1])
            c[i] = colors[i][2] + min(b[i-1], a[i-1])
        return min(a[N-1], b[N-1], c[N-1])
