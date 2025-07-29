# Problem Statement: https://practice.geeksforgeeks.org/problems/scrambled-string/1

#User function Template for python3

from collections import Counter
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str):
        if Counter(s1) != Counter(s2):
            return False
        if len(s1) == 1:
            return True
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                    (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False


#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        S1, S2 = input().split()
        if(Solution().isScramble(S1, S2)):
            print("Yes")

        else:
            print("No")


# } Driver Code Ends
