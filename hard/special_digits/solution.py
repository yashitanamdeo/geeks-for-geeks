# Problem Statement: https://practice.geeksforgeeks.org/problems/7a3e0427cbb1ea9fbfec499dc6fce377ffdf7aed/1

flag = 0
N = 10**5+5
M = 10**9+7
fact = [0]*N
invfact = [0]*N


def init():
    N = 10**5+5
    fact[0] = 1
    for i in range(1, N):
        fact[i] = (i*fact[i-1]) % M
    invfact[N-1] = pow(fact[N-1], M-2, M)
    for i in range(N-2, -1, -1):
        invfact[i] = ((i+1)*invfact[i+1]) % M


def ncr(n, r, p):
    ans = ((fact[n]*invfact[n-r] % p)*invfact[r]) % p
    return ans


class Solution:
    def bestNumbers(self, n: int, a: int, b: int, c: int, d: int) -> int:
        global flag
        if (flag == 0):
            flag = 1
            init()
        ans = 0
        if (a == b):
            Sum = n*a
            while(Sum > 0):
                if (Sum % 10 == c or Sum % 10 == d):
                    return 1
                Sum = Sum//10
            return 0
        for i in range(0, n+1):
            Sum = i*a+(n-i)*b
            good = False
            while(Sum > 0):
                if (Sum % 10 == c or Sum % 10 == d):
                    good = True
                    break
                Sum = Sum//10
            if (good):
                ans += ncr(n, i, M)
                ans %= M
        return ans


#{
 # Driver Code Starts


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = int(input())
        B = int(input())
        C = int(input())
        D = int(input())
        obj = Solution()
        res = obj.bestNumbers(N, A, B, C, D)
        print(res)
# } Driver Code Ends
