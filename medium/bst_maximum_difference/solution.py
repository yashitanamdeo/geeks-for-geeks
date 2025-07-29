# Problem Statement: https://practice.geeksforgeeks.org/problems/e841e10213ddf839d51c2909f1808632a19ae0bf/1

#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''


class Solution:
    def maxDifferenceBST(self, root, target):
        #code here
        tg_node, root_sum = self.get_target_node(root, target, 0)
        if not tg_node:
            return -1

        leaf_sum = self.tg_to_leaf_sum(tg_node, 0)
        return root_sum - (leaf_sum - tg_node.data)

    def tg_to_leaf_sum(self, tg, sum_):
        if not tg:
            return float("inf")

        if not tg.left and not tg.right:
            return sum_ + tg.data

        return min(self.tg_to_leaf_sum(tg.left, sum_ + tg.data),
                   self.tg_to_leaf_sum(tg.right, sum_ + tg.data))

    def get_target_node(self, node, target, sum_):
        if not node:
            return node, -1

        if node.data == target:
            return node, sum_

        if target < node.data:
            return self.get_target_node(node.left, target, sum_ + node.data)

        return self.get_target_node(node.right, target, sum_ + node.data)


#{
 # Driver Code Starts
#Initial Template for Python 3
class Node:
    """ Class Node """

    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node

    def traverseInorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.traverseInorder(root.left)
            self.traverseInorder(root.right)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        root = None
        tree = Tree()
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
        #tree.traverseInorder(root)
        target = int(input())

        res = Solution().maxDifferenceBST(root, target)
        print(res)

# } Driver Code Ends
