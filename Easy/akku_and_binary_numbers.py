# Problem Statement: https://practice.geeksforgeeks.org/problems/akku-and-binary-numbers0902/1

#User function Template for python3

from itertools import combinations
from bisect import bisect_left, bisect_right
class Solution:
    def solve (self, L, R):
        return bisect_right(self.valid, R) - bisect_left(self.valid, L)
        
    def precompute (self):
        self.valid = []
        for x, y, z in combinations(range(64), 3):
            self.valid.append((1<<x) + (1<<y) + (1<<z))
        self.valid.sort()
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    ob.precompute()
    t = int (input ())
    for _ in range (t):
        L, R = map(int,input().split())
        ans = ob.solve(L, R);
        print(ans)




# } Driver Code Ends