# Problem Statement: https://www.geeksforgeeks.org/problems/maximum-sum-of-non-adjacent-nodes/1

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getMaxSum(self, root):
        def dfs(cur=root):
            if not cur:
                return 0,0
            li,le=dfs(cur.left)
            ri,re=dfs(cur.right)
            return cur.data+le+re,max(li+ri,li+re,le+ri,le+re)
        return max(dfs())

