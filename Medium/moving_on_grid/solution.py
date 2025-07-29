# Problem Statement: https://practice.geeksforgeeks.org/problems/moving-on-grid1135/1

#User function Template for python3

class Solution:
    def movOnGrid(self, r, c):
	    r = (r - 1) % 7
        c = (c - 1) % 4 
	    return ["JON", "ARYA"][r==c]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		r,c =map(int,input().strip().split())
		ob = Solution();
		print(ob.movOnGrid(r,c))

# } Driver Code Ends