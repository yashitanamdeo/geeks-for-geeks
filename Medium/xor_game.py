# Problem Statement: https://practice.geeksforgeeks.org/problems/xor-game2143/1#

#User function Template for python3

# Solution 1:
class Solution:
    def xorCal(self, k):
        for i in range(1,101):
            if i ^ (i+1) == k:
                return i
        return -1

# Solution 2:
class Solution:
    def xorCal(self, k):
        if k % 2 == 0:
            return -1
            
        if (k & (k+1)) != 0:
            return -1
            
        if k == 1: 
            return 2
        
        return k>>1
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())
        
        ob = Solution()
        print(ob.xorCal(k))
# } Driver Code Ends