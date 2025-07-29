# Problem Statement: https://practice.geeksforgeeks.org/problems/perfect-numbers3207/1

# User function Template for python3

class Solution:
    def isPerfectNumber(self, N):
        i, sum = 2, 1
        while i**2 <= N:
            if N % i == 0:
                sum += (i+(N//i))
            i += 1
        if N == (i-1)**2:
            sum -= (i-1)
        return 1 if sum == N else 0


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends
