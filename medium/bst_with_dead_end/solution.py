# Problem Statement: https://www.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1

# Your task is to complete this function
# function should return true/false or 1/0
from collections import deque


class Solution:
    def isDeadEnd(self, root):
        # Initialize a queue for BFS traversal
        queue = deque()
        queue.append(root)

        # Sets to store visited nodes and leaf nodes
        visited_nodes, leaf_nodes = set(), set()

        # Perform BFS traversal
        while queue:
            current_node = queue.popleft()

            # Add current node to the visited set
            visited_nodes.add(current_node.data)

            # Enqueue left child if present
            if current_node.left:
                queue.append(current_node.left)

            # Enqueue right child if present
            if current_node.right:
                queue.append(current_node.right)

            # Add current node to the leaf set if it is a leaf node
            if not current_node.left and not current_node.right:
                leaf_nodes.add(current_node.data)

        # Check for dead ends in the leaf nodes
        for leaf in leaf_nodes:
            # If the leaf node is 1 and its next node is 2, or if the leaf node's neighbors are present, return 1
            if (leaf == 1 and 2 in visited_nodes) or (leaf - 1 in visited_nodes and leaf + 1 in visited_nodes):
                return 1

        # No dead end found
        return 0

# {
 # Driver Code Starts


class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))

        ob = Solution()
        if ob.isDeadEnd(root):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
