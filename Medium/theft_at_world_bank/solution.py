# Problem Statement: https://practice.geeksforgeeks.org/problems/theft-at-the-world-bank2156/1

#User function Template for python3
import math

class Solution:
	def maximumProfit(self, n, c, w, p):
		# Code here
        arr = []
        for i in range(n):
            if p[i] != 0:
                arr.append([w[i],p[i],w[i]/p[i]])
            else:
                arr.append([w[i],p[i],999999999])
        arr.sort(key = lambda x:x[2])
        ans = 0
        for i in range(n):
            if c == 0:
                break
            if math.sqrt(arr[i][0]) % 1 == 0:
                continue
            if c>= arr[i][0] :
                c-=arr[i][0]
                ans += arr[i][1]
            else:
                ans += (arr[i][1]/arr[i][0]) * c
                break
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, C = input().split()
		n = int(n)
		C = int(C)
		temp = list(map(int, input().split()))
		w = []
		p = []
		for i in range (2*n):
		    if(i%2) == 0:
		        w.append(temp[i])
		    else:
		        p.append(temp[i])
		ob = Solution()
		ans = ob.maximumProfit(n, C, w, p)
		print("{:.3f}".format(ans))
# } Driver Code Ends