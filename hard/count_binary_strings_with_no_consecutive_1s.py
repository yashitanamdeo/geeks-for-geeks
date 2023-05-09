# Problem Statement: https://practice.geeksforgeeks.org/problems/37f36b318a7d99c81f17f0a54fc46b5ce06bbe8c/1

# User function Template for python3
class Solution:
    m = 1000000007

    def f(self, n):
        if n == 0:
            return 0, 1
        a, b = self.f(n//2)
        c = (a*(b*2-a)) % self.m
        d = (a*a+b*b) % self.m
        if n % 2 == 1:
            return d, c+d
        return c, d

    def countStrings(self, N):
        # Code here
        ans, _ = self.f(N+2)
        return ans % self.m


# {
 # Driver Code Starts
# Initial Template for Python 3
# Initial Template for Python 3
if __name__ == '__main__':

    T = int(input())
    while T > 0:

        ob = Solution()
        print(ob.countStrings(int(input())))

        T -= 1
# } Driver Code Ends
