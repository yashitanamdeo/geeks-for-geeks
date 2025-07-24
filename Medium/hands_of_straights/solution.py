# Problem Statement: https://practice.geeksforgeeks.org/problems/hands-of-straights/1

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

from collections import Counter
import heapq


class Solution:
    def isStraightHand(self, N, groupSize, hand):
        # Code here
        v = N % groupSize
        if v:
            return False
        c = Counter(hand)
        n = list(c.keys())
        heapq.heapify(n)
        # visit={}
        while n:
            x = n[0]
            if x not in c:
                heapq.heappop(n)
                continue
            for i in range(x, x+groupSize):
                if i not in c:
                    return False
                c[i] -= 1
                if c[i] == 0:
                    del c[i]
        return True


# {
 # Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, groupSize = list(map(int, input().split()))
        hand = list(map(int, input().split()))
        ob = Solution()
        res = ob.isStraightHand(N, groupSize, hand)
        print(res)
# } Driver Code Ends
