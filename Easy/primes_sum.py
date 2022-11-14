# Problem Statement: https://practice.geeksforgeeks.org/problems/primes-sum5827/1

# User function Template for python3
class Solution:
    def isSumOfTwo(self, N):

        # code here
        if (N & 1) == 0:
            return "Yes"
        N = N-2
        for i in range(2, N):
            if N % i == 0:
                return "No"
        else:
            return "Yes"


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.isSumOfTwo(N))
# } Driver Code Ends
