# Problem Statement: https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle2948/1

#User function Template for python3


class Solution:
    def maximumSumRectangle(self,R,C,M):
        def max_sub_arr(arr):
            s = ans = arr[0]
            for i in range(1,C):
                s += arr[i]
                s = max(s,arr[i])
                ans = max(ans,s)
            return ans
        ans = M[0][0] # first cell as optimal choice
        for k in range(R):
            a = [0]*C
            for i in range(k,R):
                for j in range(C):
                    a[j]+= M[i][j]
                ans = max(ans,max_sub_arr(a))
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().strip())
    for _ in range(t):
        N,M=map(int,sys.stdin.readline().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,sys.stdin.readline().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.maximumSumRectangle(N,M,a))
# } Driver Code Ends