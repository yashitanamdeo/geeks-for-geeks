# Problem Statement: https://practice.geeksforgeeks.org/problems/shortest-unique-prefix-for-every-word/1

#User function Template for python3


class Solution:
    def findPrefixes(self, arr, N):
        z=[]
        for i in arr:
            for j in range(len(i)):
                for k in arr[0:arr.index(i)]+arr[arr.index(i)+1:]:
                    try:
                        if i[:j+1]!=k[:j+1]:
                            pass
                        else:
                            break
                    except:
                        pass
                else:
                    z.append(i[:j+1])
                    break
        return z 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(str,input().split()))
        
        ob = Solution()
        res = ob.findPrefixes(arr,N)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends