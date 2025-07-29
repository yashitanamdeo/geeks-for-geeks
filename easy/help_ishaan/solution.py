# Problem Statement: https://practice.geeksforgeeks.org/problems/help-ishaan5837/1

#User function Template for python3
import math

class Solution:
	def NthTerm(self, N):
	    if self.is_prime(N):
	        return 0
        else:
            i = 1
            while True:
                if self.is_prime(N - i) or self.is_prime(N + i):
                    return i
                else:
                    i += 1
		
    
    def is_prime(self, num):
        if num <= 1:
            return False
        upper_limit = math.floor(math.sqrt(num)) + 1
        for i in range(2, upper_limit):
            if num % i == 0:
                return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.NthTerm(N)
		print(ans)

# } Driver Code Ends