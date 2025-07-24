# Problem Statement: https://practice.geeksforgeeks.org/problems/balanced-string1627/1

# User function Template for python3

class Solution:
    def __init__(self)
        self._ALPHABETS = "abcdefghijklmnopqrstuvwxyz"

    def _sum_of_digits(self, num):
        res = 0
        while num:
            res += num % 10
            num //= 10

        return res

    def BalancedString(self,  N):
        res = [self._ALPHABETS * (N // 26), None, None]
        og_N, N = N, N % 26

        if not N:
            return res[0]

        count = ((N >> 1) + ((og_N & 1) * (1 - (self._sum_of_digits(og_N) & 1))))

        res[1] = self._ALPHABETS[: count]
        res[2] = self._ALPHABETS[26 - N + count]

        return "".join(res)

# {
 #Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int (i nput())
    f o r _ in range(t):
        N = int(input())
  
ob = Solution()
        pr i nt(ob.BalancedString(N))
# } Driver Code Ends

