# Problem Statement: https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1

# User function Template for python3

class Solution:

    # Function to merge the arrays.
    def merge(self, arr1, arr2, n, m):
        # code here
        arr1.extend(arr2)
        arr2.clear()
        return arr1.sort()


# {
 # Driver Code Starts
# Initial template for Python
if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n, m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1, end=" ")
        print(*arr2)
# } Driver Code Ends
