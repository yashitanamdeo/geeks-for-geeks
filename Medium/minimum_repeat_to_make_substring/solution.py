# Problem Statement: https://www.geeksforgeeks.org/problems/minimum-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it--170645/1

#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here 
        a = set(A)
        b = set(B)
        if b.issubset(a):
            S = ""
            ans = 0
            while len(S) < len(B):
                S += A
                ans +=1
            if B in S:
                return ans
            elif B in S+A:
                return ans + 1
            else:
                return -1
        else:
            return -1
