# Problem Statement: https://practice.geeksforgeeks.org/problems/fill-up-buckets3500/1

# User function Template for python3

class Solution:

    def totalWays(self, n, capacity):

     # code here
        capacity.sort()
        ans = 1
        mod = 1000000007
        for i in range(n):
            ans = ans*(capacity[i]-i) % mod

        return int(ans % mod)


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        capacity = list(map(int, input().split()))
        ob = Solution()
        ans = ob.totalWays(n, capacity)
        print(ans)

# } Driver Code Ends
