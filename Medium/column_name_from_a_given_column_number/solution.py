# Problem Statement: https://practice.geeksforgeeks.org/problems/column-name-from-a-given-column-number4244/1

# User function Template for python3

class Solution:
    def colName(self, n):
        ans = ""
        while n:
            n = n-1
            r = n % 26
            n = n//26
            ans = chr(ord("A")+r)+ans
        return ans


# {
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())
for tc in range(t):
    n = int(input())
    ob = Solution()
    print(ob.colName(n))


# } Driver Code Ends
