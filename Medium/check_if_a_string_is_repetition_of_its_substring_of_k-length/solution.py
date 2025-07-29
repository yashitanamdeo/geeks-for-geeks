# Problem Statement: https://www.geeksforgeeks.org/problems/check-if-a-string-is-repetition-of-its-substring-of-k-length3302/1

#User function Template for python3
class Solution:
	def diffCount(self, s1, s2):
        count = 0
        for i, j in zip(s1, s2):
            if i != j:
                count += 1
                
        return count
    
	def kSubstrConcat(self, n, s, k):
		# Your Code Here
		if n%k != 0:
		    return 0
		    
		q = n//k    
		first = s[:k]*q
		last = s[-k:]*q
		
		if self.diffCount(first, s) <= k or self.diffCount(last, s) <= k:
		    return 1
		
		return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		s = input()
		k = int(input())
		ob = Solution()
		print(ob.kSubstrConcat(n,s,k))

# } Driver Code Ends