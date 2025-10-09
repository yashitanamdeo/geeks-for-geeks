# Problem Statement: https://www.geeksforgeeks.org/problems/postorder-traversal/1

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        left = right = []
        if root.left:
            left = self.postOrder(root.left)
        if root.right:
            right = self.postOrder(root.right)
        return [*left, *right, root.data]