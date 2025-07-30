# Problem Statement: https://practice.geeksforgeeks.org/problems/-matchsticks-game4906/1

# User function Template for python3

class Solution:
    def matchGame(self, N):
        # code here
        if N % 5 == 0:
            return -1
        return N % 5


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.matchGame(N))
# } Driver Code Ends
