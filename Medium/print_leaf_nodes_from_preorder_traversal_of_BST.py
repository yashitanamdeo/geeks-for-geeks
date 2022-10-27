# Problem Statement: https://practice.geeksforgeeks.org/problems/print-leaf-nodes-from-preorder-traversal-of-bst2657/1

#User function Template for python3
class Solution:
	def leafNodes(self, arr, N):
        ans = []
        def solve(a):
            if 0 <= len(a) < 2:
                ans.extend(a)
                return
            root = a[0]
            i = 1
            while i < len(a) and root > a[i]:
                 i += 1
            solve(a[1:i])
            solve(a[i:])
        solve(arr)
        return ans



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
        ans = ob.leafNodes(arr,N)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
# } Driver Code Ends