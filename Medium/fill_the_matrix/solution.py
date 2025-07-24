# Problem Statement: https://practice.geeksforgeeks.org/problems/2145720aebf8ea0b07f76b17217b3353a0fbea7f/1

#User function Template for python3

class Solution:
    def minIteration(self, N, M, x, y):
        #code here
        return max(max(x+y-2, y+N-1-x), max(x+M-y-1, N-x+M-y))


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T = int(input())
	for i in range(T):
		N, M = map(int, input().split())
		x, y = map(int, input().split())
		ob = Solution()
		print(ob.minIteration(N, M, x, y))
# } Driver Code Ends
