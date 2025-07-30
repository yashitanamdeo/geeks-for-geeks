# Problem Statement: https://www.geeksforgeeks.org/problems/count-digit-groupings-of-a-number1520/1

#User function Template for python3

class Solution:
    def __init__(self):
        self.dp = []
        
	def TotalCount(self, s):
	    maxsum = (len(s) * (len(s) + 1)) // 2 * 9
	    self.dp = [[-1]* (maxsum + 1) for _ in range(len(s))]
	    return self.grouping(s,0,0)
	    
	def grouping(self,s,index,sum):
	    if index == len(s):
	        return 1
	   
	    if self.dp[index][sum] != -1:
	        return self.dp[index][sum]
	        
	    currSum = 0
	    ans = 0
	    
	    for i in range(index, len(s)):
	        currSum += int(s[i])
	        
	        if currSum >= sum:
	            ans += self.grouping(s,i+1,currSum)
	            
	    self.dp[index][sum] = ans
	    
	    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.TotalCount(s)
		print(ans)
# } Driver Code Ends