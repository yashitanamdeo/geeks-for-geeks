# Problem Statement: https://practice.geeksforgeeks.org/problems/cf0cd86c66d07222499f84ec22dbcf6cae30e848/1

#User function Template for python3

class Solution:
    def LCP(self,arr,n):
        min_i = min(range(n), key=lambda i: arr[i])
        max_i = max(range(n), key=lambda i: arr[i])
        i = 0
        while i < min(len(arr[min_i]), len(arr[max_i])):
            if arr[min_i][i] != arr[max_i][i]:
                break
            i += 1
        return arr[min_i][:i] or -1
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs =int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[ x  for x in input().split()]
        obj=Solution()
        print(obj.LCP(arr,n))
# } Driver Code Ends