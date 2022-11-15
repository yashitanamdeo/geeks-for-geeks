# Problem Statement: https://practice.geeksforgeeks.org/problems/close-to-perfection1525/1

# User function Template for python3

import sys


class Solution:
    def longestPerfectPiece(self, arr, N):
        # code here
        flg, count, f1, f2 = 0, 0, 0, 0
        len = -sys.maxsize - 1
        for i in range(N):

            for j in range(f1, N):
                if arr[i]-arr[j] == 1 or arr[i] == arr[j]:
                    if len < abs(i-j):
                        len = abs(i-j)
                else:
                    f1 = j
                    break

            for j in range(f2, N):
                if arr[i]-arr[j] == -1 or arr[i] == arr[j]:
                    if len < abs(i-j):
                        len = abs(i-j)
                else:
                    f2 = j
                    break
        return len+1


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        print(ob.longestPerfectPiece(arr, N))
# } Driver Code Ends
