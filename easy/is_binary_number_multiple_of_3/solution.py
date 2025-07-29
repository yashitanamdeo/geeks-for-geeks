# Problem Statement: https://practice.geeksforgeeks.org/problems/is-binary-number-multiple-of-30654/1

# User function Template for python3
class Solution:

    def isDivisible(self, s):
        odd, even, pos = 0, 0, 0
        for i in s:
            if i == "1":
                if pos % 2 == 0:
                    odd += 1
                else:
                    even += 1
            pos += 1
        return 1 if not abs(odd-even) % 3 else 0

# {
 # Driver Code Starts

# Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ob = Solution()
        ans = ob.isDivisible(s)
        print(ans)

# } Driver Code Ends
