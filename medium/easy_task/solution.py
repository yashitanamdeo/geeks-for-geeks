# Problem Statement: https://practice.geeksforgeeks.org/problems/c928f229cc972671d91c5e9f6b222414912cc88a/1

from typing import List


def merge(a, b):
    return [a[i]+b[i] for i in range(len(a))]


class SegmentTree:

    def __init__(self, s):
        n = len(s)
        self.tree = [[0]*26 for _ in range(2*n)]
        self.n = n
        for i in range(n):
            idx = ord(s[i])-ord('a')
            self.tree[i+n][idx] += 1

        for i in range(n-1, 0, -1):
            self.tree[i] = merge(self.tree[i*2], self.tree[i*2+1])

    def update(self, i, c):
        i = i+self.n
        self.tree[i] = [0]*26
        self.tree[i][ord(c)-ord('a')] = 1
        while i > 1:
            i //= 2
            self.tree[i] = merge(self.tree[i*2], self.tree[i*2+1])

    def query(self, l, r):
        ans = [0]*26
        l += self.n
        r += self.n
        while l <= r:
            if l % 2 == 1:
                ans = merge(ans, self.tree[l])
                l += 1
            if r % 2 == 0:
                ans = merge(ans, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return ans


class Solution:
    def easyTask(self, n, s, q, queries) -> List[int]:
        ans = []
        st = SegmentTree(s)
        for t, *q in queries:
            if t == "1":
                st.update(int(q[0]), q[1])
            else:
                l, r, k = map(int, q)
                freq = st.query(l, r)
                for c in range(25, -1, -1):
                    k -= freq[c]
                    if k <= 0:
                        ans.append(chr(97+c))
                        break
        return ans


# {
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        q = int(input())
        queries = []
        for i in range(q):
            quer = input().split()
            if quer[0] == "1":
                queries.append([quer[0], quer[1], quer[2]])
            else:
                queries.append([quer[0], quer[1], quer[2], quer[3]])

        ob = Solution()
        res = ob.easyTask(n, s, q, queries)

        IntArray().Print(res)


# } Driver Code Ends
