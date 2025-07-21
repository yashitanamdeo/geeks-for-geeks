# Problem Statement: https://www.geeksforgeeks.org/problems/rotate-and-delete-1587115621/1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

# from typing import List


class Solution:
    def rotateDelete(self,  arr):
        n = len(arr)
        for k in range(1, n // 2 + 1):
            arr.insert(0, arr.pop())
            arr.pop(-k)
        return arr[0]
        


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.rotateDelete(arr)
        print(res)
        t -= 1


# } Driver Code Ends