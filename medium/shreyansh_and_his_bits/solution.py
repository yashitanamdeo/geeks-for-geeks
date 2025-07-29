# Problem Statement: https://practice.geeksforgeeks.org/problems/shreyansh-and-his-bits1420/1

class Solution:
    def count(self, N):
        # code here

        dp = [[-1]*(50) for _ in range(50)]

        def solve(spots, ones):
            if ones > spots:
                return 0
            if ones == 0 or ones == spots:
                return 1
            if dp[spots][ones] != -1:
                return dp[spots][ones]

            res = solve(spots-1, ones-1)+solve(spots-1, ones)
            dp[spots][ones] = res
            return res

        out = 0
        ones = 0
        bits = 0
        while N != 0:
            if N & 1:
                out += solve(bits, ones+1)
                ones += 1
            bits += 1
            N >>= 1
        return out


#{
 # Driver Code Starts
if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        N = int(input())
        print(ob.count(N))


# } Driver Code Ends
