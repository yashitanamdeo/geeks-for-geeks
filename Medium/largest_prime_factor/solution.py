# Problem Statement: https://practice.geeksforgeeks.org/problems/largest-prime-factor2601/1

# User function Template for python3

class Solution:
    def isPrime(self, n):
        if n == 1:
            return False
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    def largestPrimeFactor(self, n):
        i = 2
        while i*i < n:
            i += 1
        while i >= 1:
            if n % i == 0:
                if self.isPrime(i) and self.isPrime(n//i):
                    return max(i, n//i)
                elif self.isPrime(i):
                    return i
                elif self.isPrime(n//i):
                    return n//i
            i = i - 1


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends
