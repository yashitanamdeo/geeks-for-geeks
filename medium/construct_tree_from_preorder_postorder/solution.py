# Problem Statement: https://www.geeksforgeeks.org/problems/construct-tree-from-preorder-postorder/1

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def constructTree(self, pre, post):
        post_index = {val: i for i, val in enumerate(post)}
        n = len(pre)

        def build(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None
            root = Node(pre[pre_start])
            if pre_start == pre_end:
                return root

            # Next node in preorder is left child
            left_root_val = pre[pre_start + 1]
            left_root_index = post_index[left_root_val]
            left_size = left_root_index - post_start + 1

            root.left = build(pre_start + 1, pre_start + left_size, post_start, left_root_index)
            root.right = build(pre_start + left_size + 1, pre_end, left_root_index + 1, post_end - 1)
            return root

        return build(0, n - 1, 0, n - 1)