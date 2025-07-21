# Problem Statement: https://practice.geeksforgeeks.org/problems/93c977e771fc0d82e87ba570702732edb2226ad7/1

# User function Template for python3

class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def constructBinaryTree(self, pre, preMirror, size):
        # code here
        def create_a_tree(left, right):
            if left > right:
                return None
            mid = (left+right)//2
            node = TreeNode(pre[left])
            node.left = create_a_tree(left+1, mid)
            node.right = create_a_tree(mid+1, right)
            return node
        root = create_a_tree(0, len(pre)-1)
        return root


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    def printInorder(node):
        if node == None:
            return
        printInorder(node.left)
        print(node.data, end=" ")
        printInorder(node.right)

    test_cases = int(input())
    for _ in range(test_cases):
        N = int(input())
        pre = list(map(int, input().split()))
        preMirror = list(map(int, input().split()))
        res = Solution().constructBinaryTree(pre, preMirror, N)
        if printInorder(res) != None:
            print(printInorder(res)[:len(printInorder(res))-2])
        print()
# } Driver Code Ends
