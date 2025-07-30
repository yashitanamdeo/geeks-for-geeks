# Problem Statement: https://practice.geeksforgeeks.org/problems/quick-sort/1

#User function Template for python3

class Solution:
    def quickSort(self,arr,low,high):
        if low<high:
            p=self.partition(arr,low,high)
            self.quickSort(arr,low,p-1)
            self.quickSort(arr,p+1,high)
        
    def partition(self,arr,low,high):
        x=low
        for i in range(low,high):
            if arr[i]<=arr[high]:
                arr[x],arr[i]=arr[i],arr[x]
                x+=1
        arr[x],arr[high]=arr[high],arr[x]
        return x
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends