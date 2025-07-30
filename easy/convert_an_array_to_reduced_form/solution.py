# Problem Statement: https://practice.geeksforgeeks.org/problems/convert-an-array-to-reduced-form1101/1

# User function Template for python3
class Solution:
    def convert(self, arr, n):
        res = arr.copy()
        res.sort()
        dic = {}
        for i in range(len(arr)):
            dic[res[i]] = i

        for index, i in enumerate(arr):
            val = dic[i]
            arr[index] = val
            index += 1

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
