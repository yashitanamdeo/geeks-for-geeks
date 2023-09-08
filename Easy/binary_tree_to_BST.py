# Problem Statement: https://practice.geeksforgeeks.org/problems/binary-tree-to-bst/1

# User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import deque


class Solution:
    def inorder(self, root, v):
        if not root:
            return
        self.inorder(root.left, v)
        v.append(root.data)
        self.inorder(root.right, v)

    def fill_it(self, root, v, ind):
        if not root:
            return
        self.fill_it(root.left, v, ind)
        root.data = v[ind[0]]
        ind[0] += 1
        self.fill_it(root.right, v, ind)

    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        # code here
        v = []
        # STEP 1 : Do inorder traversal and store each node data in array or list
        self.inorder(root, v)
        # STEP 2 : Sort the array or List
        v.sort()
        ind = [0]
        # STEP 3: Update the Binary tree to make it BST
        self.fill_it(root, v, ind)
        return root


# {
 # Driver Code Starts
# Initial Template for Python 3

# Tree Node


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree


def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size+1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size-1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):

            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size+1
        # For the right child
        i = i+1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):

            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size+1
        i = i+1
    return root


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end=' ')
    printInorder(root.right)


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root = buildTree(s)
        Solution().binaryTreeToBST(root)
        printInorder(root)
        print()
# } Driver Code Ends
