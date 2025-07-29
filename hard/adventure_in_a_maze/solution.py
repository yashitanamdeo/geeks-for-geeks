# Problem Statement: https://practice.geeksforgeeks.org/problems/adventure-in-a-maze2051/1

#User function Template for python3

from itertools import product

MOD = int(1e9 + 7)

class Solution:
    def FindWays(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[(0, 0) for _ in range(n)] for __ in range(m)]
        dp[0][0] = (1, matrix[0][0])

        for i in range(1, m):
            if matrix[i - 1][0] == 1:
                break
            val = dp[i - 1][0][1]
            dp[i][0] = (1, val + matrix[i][0])

        for j in range(1, n):
            if matrix[0][j - 1] == 2:
                break
            val = dp[0][j - 1][1]
            dp[0][j] = (1, val + matrix[0][j])

        for i, j in product(range(1, m), range(1, n)):
            cnt_top, val_top = dp[i - 1][j]
            cnt_left, val_left = dp[i][j - 1]
            cnt, val = 0, 0

            if matrix[i - 1][j] != 1 and cnt_top:
                cnt = cnt_top % MOD
                val = val_top + matrix[i][j]

            if matrix[i][j - 1] != 2 and cnt_left:
                cnt = (cnt + cnt_left) % MOD
                val = max(val, val_left + matrix[i][j])

            dp[i][j] = (cnt, val)

        return list(dp[m - 1][n - 1])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			cur = list(map(int, input().split()))
			matrix.append(cur)
		obj = Solution()
		ans = obj.FindWays(matrix)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends