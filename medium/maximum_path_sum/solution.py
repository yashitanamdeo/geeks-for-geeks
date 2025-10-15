# Problem Statement: https://www.geeksforgeeks.org/problems/maximum-path-sum-from-any-node/1

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def __init__(self):
        self.res = -sys.maxsize
        
    def dfs(self, root):
        r1 = r2 = 0
        if root.left:
            r1 = self.dfs(root.left)

        if root.right:
            r2 = self.dfs(root.right)
        
        self.res = max(self.res, r1 + root.data, r2 + root.data, root.data, r1 + r2 + root.data)
        
        res = max(r1, r2) + root.data

        return 0 if res < 0 else res

        
    def findMaxSum(self, root): 
        # code here
        self.dfs(root)
        return self.res