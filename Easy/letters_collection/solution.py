# Problem Statement: https://www.geeksforgeeks.org/problems/c-letters-collection4552/1

# User function Template for python3

class Solution:
    def matrixSum(self, n, m, mat, q, queries):
        from itertools import chain, product
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def get_diffs(d):
            return list(chain(
                product([-d], range(-d, d + 1)),
                product(range(-d + 1, d), [-d, d]),
                product([d], range(-d, d + 1))
            ))

        def get_neighbor_numbers(d, x, y):
            return [
                mat[x + dx][y + dy]
                for dx, dy in get_diffs(d)
                if 0 <= x + dx < n and 0 <= y + dy < m
            ]

        return [sum(get_neighbor_numbers(*q_args)) for q_args in queries]

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = [[0]*m for x in range(n)]
        for i in range(n):
            arr = input().split()
            for j in range(m):
                mat[i][j] = int(arr[j])
        q = int(input())
        queries = [[0]*3 for x in range(q)]
        for i in range(q):
            a = input().split()
            for j in range(3):
                queries[i][j] = int(a[j])

        ob = Solution()
        ans = ob.matrixSum(n, m, mat, q, queries)
        for i in range(q):
            print(ans[i])
# } Driver Code Ends
