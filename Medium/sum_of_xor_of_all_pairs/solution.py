# Problem Statement: https://practice.geeksforgeeks.org/problems/sum-of-xor-of-all-pairs0723/1

# User function Template for python3

class Solution:
    def sumXOR(self, arr, n):
        ans = 0
        for i in range(32):
            ones = 0
            for x in arr:
                ones += (1 if (x & (1 << i)) else 0)
            ans += (ones * (n - ones) * (1 << i))
        return ans


# {
 # Driver Code Starts
# Initial Template for Python 3


for _ in range(0, int(input())):

    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends
