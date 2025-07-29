# Problem Statement: https://practice.geeksforgeeks.org/problems/maximum-sub-string-after-at-most-k-changes3220/1

# User function Template for python3

from collections import defaultdict


class Solution:

    def characterReplacement(self, s, k):

        c = defaultdict(int)
        res, maxcount = 0, 0

        for idx, val in enumerate(s):
            c[val] += 1
            maxcount = max(maxcount, c[val])
            if res - maxcount >= k:
                c[s[idx - res]] -= 1
            else:
                res += 1
        return res


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        k = int(input())
        ob = Solution()
        ans = ob.characterReplacement(s, k)
        print(ans)

# } Driver Code Ends
