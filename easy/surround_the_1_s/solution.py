# Problem Statement: https://practice.geeksforgeeks.org/problems/surround-the-1s2505/1

# User function Template for python3

class Solution:
    def Count(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        result = 0
        for i in range(m):
            for j in range(n):
                count = 0
                if matrix[i][j] == 1:
                    if i-1 >= 0:
                        if matrix[i-1][j] == 0:
                            count += 1
                    if i+1 < m:
                        if matrix[i+1][j] == 0:
                            count += 1
                    if j-1 >= 0:
                        if matrix[i][j-1] == 0:
                            count += 1
                    if j + 1 < n:
                        if matrix[i][j+1] == 0:
                            count += 1
                    if i-1 >= 0 and j-1 >= 0:
                        if matrix[i-1][j-1] == 0:
                            count += 1
                    if i-1 >= 0 and j+1 < n:
                        if matrix[i-1][j+1] == 0:
                            count += 1
                    if i+1 < m and j - 1 >= 0:
                        if matrix[i+1][j-1] == 0:
                            count += 1
                    if i+1 < m and j+1 < n:
                        if matrix[i+1][j+1] == 0:
                            count += 1
                if count % 2 == 0 and count != 0:
                    result += 1
        return result


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.Count(matrix)
        print(ans)

# } Driver Code Ends
