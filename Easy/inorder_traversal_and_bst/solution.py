# Problem Statement: https://www.geeksforgeeks.org/problems/inorder-traversal-and-bst5855/1

#User function Template for python3

class Solution:
    def isRepresentingBST(self, arr, N):
        # code here
        return 1 if arr==sorted(arr) else 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.isRepresentingBST(arr, N))
# } Driver Code Ends