# Problem Statement: https://practice.geeksforgeeks.org/problems/3d49e4cce2820a813da02d1587c2dd9c542ce769/1

#User function Template for python3

from collections import Counter
class Solution:
    def countSpecialNumbers(self, N, arr):
        # Code here
        arr.sort()
        d=Counter(arr)
        c=0
        for i in range(N):
            if d[arr[i]]>1:
                c+=1
            else:
                j=0
                while j<i:
                    if arr[i]%arr[j]==0:
                        c+=1
                        break
                    j+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.countSpecialNumbers(N, arr))
        
        T -= 1
# } Driver Code Ends