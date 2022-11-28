# Problem Statement: https://practice.geeksforgeeks.org/problems/maximum-sub-array5443/1

#User function Template for python3

class Solution:
	def findSubarray(self, a, n):
	        # code here
            start = 0
            stop = -1
            i, j, mx, sm = 0, 0, 0, 0
            while j < n:
                if a[j] >= 0:
                    sm += a[j]
                    j += 1
                else:
                    if mx < sm:
                        mx = sm
                        start = i
                        stop = j-1
                    sm = 0
                    j += 1
                    i = j
            if mx < sm:
                mx = sm
                start = i
                stop = j-1
            res = []
            # print(start, stop)
            for i in range(start, stop+1):
                res.append(a[i])
            if len(res) == 0:
                res.append(-1)
            return res


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc = int(input())
	while tc > 0:
	    n = int(input())
	    a = list(map(int, input().strip().split()))
	    ob = Solution()
	    ans = ob.findSubarray(a, n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc = tc-1
# } Driver Code Ends
