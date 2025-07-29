# Problem Statement: https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1

# User function Template for python3

class Solution:
    def pushZerosToEnd(self, arr, n):
        pos = 0

        for i in range(n):
            if arr[i] != 0:
                arr[pos], arr[i] = arr[i], arr[pos]
                pos += 1


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends
