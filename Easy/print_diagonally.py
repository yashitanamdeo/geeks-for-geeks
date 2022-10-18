# Problem Statement: https://practice.geeksforgeeks.org/problems/print-diagonally4331/1

#User function Template for python3

from collections import defaultdict


def downwardDigonal(N, A):
    # code here
    d = defaultdict(list)
    for i in range(N):
        for j in range(N):
            d[i+j].append(A[i][j])
    ans = []
    for i in d:
        for j in d[i]:
            ans.append(j)
    return ans


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = []
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n, matrix)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends
