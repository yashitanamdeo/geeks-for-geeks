# Problem Statement: https://practice.geeksforgeeks.org/problems/floor-in-bst/1

# User function Template for python3

class Solution:
    def floor(self, root, x):
        curr = root
        result = -1
        while curr:
            if curr.data == x:
                return x
            elif curr.data > x:
                curr = curr.left
            else:
                result = curr.data
                curr = curr.right
        return result


# {
 # Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def insert(tree, val):
    if (tree == None):
        return Node(val)
    if (val < tree.data):
        tree.left = insert(tree.left, val)
    elif (val > tree.data):
        tree.right = insert(tree.right, val)
    return tree


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        arr = list(map(int, input().split()))
        root = None
        for k in arr:
            root = insert(root, k)
        s = int(input())
        obj = Solution()
        print(obj.floor(root, s))
# } Driver Code Ends
