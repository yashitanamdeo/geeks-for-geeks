# Problem Statement: https://www.geeksforgeeks.org/problems/distribute-candies-in-a-binary-tree/1

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.moves = 0  

    def distCandy(self, root):
        def dfs(node):
            if not node:
                return 0
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)
            self.moves += abs(left_balance) + abs(right_balance)
            return node.data + left_balance + right_balance - 1

        dfs(root)
        return self.moves