# Problem Statement: https://www.geeksforgeeks.org/problems/bst-to-greater-sum-tree/1

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inorder(self,root):
        if root:
            self.inorder(root.right)
            self.greatSum,root.data=self.greatSum+root.data,self.greatSum
            self.inorder(root.left)
    
    def transformTree(self, root):
        self.greatSum=0
        self.inorder(root)
        return root