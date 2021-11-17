""" Problem Link: https://practice.geeksforgeeks.org/problems/the-dice-problem2316/1/?difficulty[]=-2&page=1&query=difficulty[]-2page1"""

#User function Template for python3

class Solution:
    def oppositeFaceOfDice(self, N):
    	#code here
    	return 7-N

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.oppositeFaceOfDice(N)
        print(ans)
# } Driver Code Ends