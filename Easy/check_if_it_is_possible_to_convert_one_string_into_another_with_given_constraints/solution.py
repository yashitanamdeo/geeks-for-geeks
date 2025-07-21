# Problem Statement: https://practice.geeksforgeeks.org/problems/check-if-it-is-possible-to-convert-one-string-into-another-with-given-constraints4116/1

#User function Template for python3

import math


class Solution:
    def isItPossible(self, S, T, M, N):
        if M != N:
            return 0
        balance = 0  # neg means A, pos means B
        for s, t in zip(S, T):
            if balance < 0:
                if s == 'B' or t == 'B':
                    return 0
                if t == 'A':
                    balance -= 1
                if s == 'A':
                    balance += 1
            elif balance == 0:
                if s != t:
                    if s == '#' and t == 'A':
                        balance -= 1
                    elif s == 'B' and t == '#':
                        balance += 1
                    else:
                        return 0
            else:
                if s == 'A' or t == 'A':
                    return 0
                if s == 'B':
                    balance += 1
                if t == 'B':
                    balance -= 1

        return 1 if balance == 0 else 0

#{
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, T = input().split()
        ob = Solution()
        print(ob.isItPossible(S, T, len(S), len(T)))
# } Driver Code Ends
