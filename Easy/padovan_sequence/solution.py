# Problem Statement: https://www.geeksforgeeks.org/problems/padovan-sequence2855/1

#User function Template for python3

class Solution:
    def padovanSequence(self, n):
        if n <= 2:
            return 1
        pprev, prev, curr = 1, 1, 1
        for _ in range(3, n + 1):
            pprev, prev, curr = prev, curr, (prev + pprev) % (10 ** 9 + 7)
        return curr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.padovanSequence(n))

# } Driver Code Ends