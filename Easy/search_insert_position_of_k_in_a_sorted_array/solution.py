# Problem Statement: https://practice.geeksforgeeks.org/problems/search-insert-position-of-k-in-a-sorted-array/1

#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        if k not in Arr:
            Arr.append(k)
        Arr.sort()
        return Arr.index(k)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends