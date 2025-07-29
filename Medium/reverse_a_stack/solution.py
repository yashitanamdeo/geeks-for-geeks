# Problem Statement: https://practice.geeksforgeeks.org/problems/reverse-a-stack/1

# User function Template for python3

from typing import List


class Solution:
    def reverse(self, St):
        temp = []
        while St:
            temp.append(St.pop())

        n = len(temp)

        for i in range(n):
            St.append(temp[i])


# {
 # Driver Code Starts

# Initial Template for Python 3


for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
# } Driver Code Ends
