# Problem Statement: https://practice.geeksforgeeks.org/problems/positive-negative-pair5209/1# 

#User function Template for python3

class Solution:
    #Function to return list containing all the pairs having both
    #negative and positive values of a number in the array.
    def findPairs(self,arr,n):
        # code here 
        d=dict()
        pair=[]
        for a in arr:
            a=abs(a)
            d[a]=d.get(a,0)+1
            if d[a]==2: 
                pair.extend([-a,a])
            
        return pair
        '''ans = []
        for i in range(n):
            for j in range(i+1,n):
                if(abs(arr[i]) == abs(arr[j])):
                    ans.append(abs(arr[i]))
                    
        
        final = []
        for i in range(len(ans)):
            final.append(-ans[i])
            final.append(ans[i])
        return final'''
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        res=Solution().findPairs(arr,n)
        if len(res) == 0:
            print(0)
        else:    
            for x in res:
                print(x,end=' ')
            print()
# } Driver Code Ends