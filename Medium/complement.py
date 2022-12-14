# Problemm Statement: https://practice.geeksforgeeks.org/problems/complement3911/1

#User function Template for python3
class Solution:
    def findRange(self, a, size):
        total = 0
        curr_count = 0
        l = 0
        ans = [-1]
        for r, c in enumerate(a):
               if c == '1':
                    curr_count -= 1
                if c == '0':
                    curr_count += 1
                if curr_count > total:
                    total = curr_count
                    ans = [l+1, r+1]
                if curr_count < 0:
                    curr_count = 0
                    l = r+1
        return ans


#{
 # Driver Code Starts
if __name__ == '__main__':

	tc = int(input())
	while tc > 0:
	    n = int(input())
	    s = input()
	    ob = Solution()
	    ans = ob.findRange(s, n)
	    if len(ans) == 1:
	        print(ans[0])
	    else:
	        print(str(ans[0])+" "+str(ans[1]))
	    tc = tc-1
# } Driver Code Ends
