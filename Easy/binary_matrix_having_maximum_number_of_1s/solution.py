# Problem Statement: https://practice.geeksforgeeks.org/problems/77e1c3e12cd148f835d53eb168d4472b2ff539fa/1

#User function Template for python3

class Solution:
    def findMaxRow(self, mat, N):
        # Code here
        row = 0
        ans = 0
        for i in range(N):
            count = 0
            for j in mat[i]:
                if j == 1:
                    count += 1
            if ans < count:
                ans = count
                row = i
        return [row, ans]

#{
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat = []
        for i in range(n):
            A = [int(x) for x in input().split()]
            mat.append(A)
        ob = Solution()
        ans = []
        ans = ob.findMaxRow(mat, n)
        for i in range(2):
            print(ans[i], end=" ")
        print()
# } Driver Code Ends
