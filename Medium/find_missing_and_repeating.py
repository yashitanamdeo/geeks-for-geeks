# Problem Statement: https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1

#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        ans=[]
        arr2=arr.copy()
        for i in range(n):
            if arr[abs(arr[i])-1]<0:
                double = abs(arr[i])
            else:
                arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
        arr2.remove(double)
        s1=n*(n+1)//2
        s2=0
        for i in arr2:
            s2+=i
        mis=s1-s2
        ans.append(double)
        ans.append(mis)        
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends