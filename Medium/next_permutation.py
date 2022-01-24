# Problem Statement: https://practice.geeksforgeeks.org/problems/next-permutation5226/1

#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
       # code here
        if(N==1): return arr
        i = N-2
        j = N-1
        while(i>=0 and arr[i] > arr[i+1]):
            i -= 1
        if(i == -1): return arr[::-1]
        while(j>=0 and arr[j]<arr[i]):
            j -= 1
        arr[i],arr[j] = arr[j],arr[i]
        arr[i+1:] = reversed(arr[i+1:])
      
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends