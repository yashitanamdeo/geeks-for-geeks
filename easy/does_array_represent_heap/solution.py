# Problem Statement: https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1


class Solution:
    def isMaxHeap(self,arr,n):
        for i in range(n):
            lt = 2*i + 1
            rt = 2*i + 2
            if lt < n and arr[i] < arr[lt]:
                return False
            if rt < n and arr[i] < arr[rt]:
                return False
        return True

#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends