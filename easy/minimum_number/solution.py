# Problem Statement: https://practice.geeksforgeeks.org/problems/7d62c8606123a199720c9b6885249dc9ac651bb7/1

#User function Template for python3
#susovan
import math


class Solution:
    def minimumNumber(self, n, arr):
        #code here
        ans = arr[0]
        for i in range(1, n):
            ans = math.gcd(ans, arr[i])
        return ans


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]
        obj = Solution()
        print(obj.minimumNumber(n, arr))
# } Driver Code Ends
