# Problem Statement: https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def __init__(self):
        self.map = {}

    def traverse(self, root, val = 0, depth = 0):
        if val not in self.map or self.map[val][0] <= depth:
            self.map[val] = (depth, root.data)
        
        if root.left:
            self.traverse(root.left, val - 1, depth + 1)
            
        if root.right:
            self.traverse(root.right, val + 1, depth + 1)
        
    def bottomView(self, root):
        # code here
        res = []
        self.traverse(root)
        for k in sorted(self.map):
            res.append(self.map[k][1])
        return res