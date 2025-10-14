# Problem Statement: https://www.geeksforgeeks.org/problems/range-sum-of-bst/1

"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def nodeSum(self, root, l, r):
        
        def dfs(node):
            if node is None:
                return 0
            if node.data < l:
                return dfs(node.right)
            elif node.data > r:
                return dfs(node.left)
            else:
                return dfs(node.left) + node.data + dfs(node.right)
        
        return dfs(root)