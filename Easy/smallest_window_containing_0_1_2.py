# Problem Statement: https://practice.geeksforgeeks.org/problems/d6e88f06b273a60ae83992314ac514f71841a27d/1

#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
           
        lstind = [-1,-1,-1]
        ans = 1000000
       
        for index, item in enumerate(S):
            lstind[int(item)] = index+1
            if -1 not in lstind:

                ans = min(ans, max(lstind)- min(lstind))
       
        if ans == 1000000:
            return -1
        return ans + 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends