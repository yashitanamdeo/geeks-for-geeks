# Problem Statement: https://practice.geeksforgeeks.org/problems/rotate-bits4524/1

# User function Template for python3

class Solution:
    def rotate(self, n, d):
        d = d % 16
        x, y = (n >> (16-d)), n & ((1 << d)-1)
        return [((n-(x << (16-d))) << d)+x, ((y << (16-d))+(n >> d))]


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends
