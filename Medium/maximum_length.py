# Problem Statement: https://practice.geeksforgeeks.org/problems/84963d7b5b84aa24f7807d86e672d0f97f41a4b5/1

# User function Template for python3

from collections import Counter


class Solution():
    def solve(self, a, b, c):
        arr = [a, b, c]
        arr.sort(reverse=True)
        if arr[0] / 2 > arr[1]+arr[2]+1:
            return -1
        else:
            return sum(arr)


# {
 # Driver Code Starts
# Initial Template for Python 3

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    obj = Solution()
    res = obj.solve(a, b, c)

    print(res)
# } Driver Code Ends
