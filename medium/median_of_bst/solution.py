# Problem Statement: https://www.geeksforgeeks.org/problems/median-of-bst/1

'''
class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMedian(self, root):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left)+ [node.data]+inorder(node.right)
        lst=inorder(root)
        if len(lst)%2==0:
            return lst[len(lst)//2-1]
        else:
            return lst[(len(lst)+1)//2-1] 

