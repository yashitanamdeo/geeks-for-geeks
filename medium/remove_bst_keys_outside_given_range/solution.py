# Problem Statement: https://www.geeksforgeeks.org/problems/remove-bst-keys-outside-given-range/1

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def removekeys(self, root, l, r):
        if not root:
            return None
        if root.data < l:
            return self.removekeys(root.right, l, r)
        if root.data > r:
            return self.removekeys(root.left, l, r)
        root.left = self.removekeys(root.left, l, r)
        root.right = self.removekeys(root.right, l, r)
        return root