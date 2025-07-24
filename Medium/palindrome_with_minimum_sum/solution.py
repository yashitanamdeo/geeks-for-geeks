# Problem Statement: https://practice.geeksforgeeks.org/problems/32dc957908c2eb8beeeaeedf81f37df20d37c308/1

import math


class Solution:
    def minimumSum(self, s: str) -> int:
        # code here
        ans = 0
        s = list(s)
        n = len(s)
        for i in range(n//2):
            if s[i] == '?' and s[n-i-1] != '?':
                s[i] = s[n-i-1]
            elif s[i] != s[n-i-1] and s[i] != '?' and s[n-i-1] != '?':
                return -1
        prev = '.'
        for i in range(n//2):
            if s[i] != '?':
                if prev == '.':
                    prev = s[i]
                elif s[i] != prev:
                    ans += abs(ord(s[i])-ord(prev))
                prev = s[i]
        return ans*2


# {
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.minimumSum(s)

        print(res)


# } Driver Code Ends
