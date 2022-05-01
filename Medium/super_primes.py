# Problem Statement: https://practice.geeksforgeeks.org/problems/super-primes2443/1

# User function Template for python3
class Solution:
    def superPrimes(self, n):
    		# code here
    		ans = 0
    		primes = [True for i in range(n+1)]
            def prime(n):
                i = 2
                primes[0] = False
                primes[1] = False
                while(i*i <= n):
                    if primes[i] == True:
                        for k in range(i+i,n+1,i):
                            primes[k] = False
                    i+=1
            prime(n)
            arr = []
            for each in range(len(primes)):
                if primes[each]:
                    arr.append(each)
            for num in arr:
                if primes[num]:
                    if primes[num-2]:
                        ans += 1
            # print(primes)
            return ans

# { 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.superPrimes(n)
		print(ans)

# } Driver Code Ends
