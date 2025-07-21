# Problem Statement: https://www.geeksforgeeks.org/problems/largest-subsquare-surrounded-by-x0558/1

#User function Template for python3

class Solution:
    def largestSubsquare(self, n, a):
        row_by=[[0]*n for _ in range(n)]
        col_by=[[0]*n for _ in range(n)]
        for i in range(n):
            row=0
            col=0
            for j in range(n):
                if a[i][j]=="X":
                    row+=1
                else:
                    row=0
                row_by[i][j]=row
                if a[j][i]=="X":
                    col+=1
                else:
                    col=0
                col_by[j][i]=col
        res=0
        for i in range(n):
            for j in range(n):
                side=min(row_by[i][j],col_by[i][j])
                while side>res:
                    if row_by[i-side+1][j]>=side and col_by[i][j-side+1]>=side:
                        res=side
                    else:
                        side-=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[]
        for i in range(n):
            s=list(map(str,input().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.largestSubsquare(n,a))
# } Driver Code Ends