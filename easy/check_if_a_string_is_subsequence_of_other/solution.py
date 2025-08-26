# Problem Statement: https://www.geeksforgeeks.org/problems/given-two-strings-find-if-first-string-is-a-subsequence-of-second/1

class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        l = len(s1)
        mi = 0
        
        for ch in s2:
            if mi < l and s1[mi] == ch:
                mi += 1
     
        return mi == l