# Problem Statement: https://practice.geeksforgeeks.org/problems/rank-the-permutations2229/1

#User function Template for python3

class Solution:
	def findRank(self, s):
		#Code 
		factorial = [0 for _ in range(27)]
		factorial[1] = 1
		for i in range(2,27):
		    factorial[i] = factorial[i-1]*i
		arr = [0 for i in range(27)]
		for c in s:
		    arr[ord(c)-ord('a')] = 1
		rank = 0 
		for i in range(len(s)):
		    countl = 0
		    for j in range(27):
		        if ord(s[i])-ord('a') == j:
		            break
		        elif arr[j]:
		            countl+= 1
		    arr[ord(s[i])-ord('a')] = 0
		    rank += countl*factorial[len(s)-1-i]
        return rank+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	str = input().strip()
    	obj = Solution()
    	ans = obj.findRank(str)
    	print(ans)
# } Driver Code Ends