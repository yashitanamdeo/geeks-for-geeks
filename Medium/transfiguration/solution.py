# Problem Statement: https://practice.geeksforgeeks.org/problems/b6b3297ccfb1ad5f66a9c2b92979170417adf114/1#

#User function Template for python3

class Solution:
    def transfigure(self, A, B):
        from collections import Counter
        if Counter(A) != Counter(B):
            return -1
        
        i = j = len(A) - 1
    	while i >= 0:
    	    if A[i] == B[j]: 
    	        j -= 1
    	    i -= 1
    	
    	return j + 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        obj = Solution();
        print(obj.transfigure(A,B))


# } Driver Code Ends