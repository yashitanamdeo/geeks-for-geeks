# Problem Statement: https://practice.geeksforgeeks.org/problems/print-common-nodes-in-bst/1

# User function Template for python3

# Define a class 'Node' to represent a node in a Binary Search Tree (BST).
from collections import deque


class Node:
    def __init__(self, v):
        self.data = v
        self.left = None  # Initialize the left child as None.
        self.right = None  # Initialize the right child as None.

# Define a class 'Solution' to solve the problem of finding common elements in two BSTs.


class Solution:

    # Function to perform an in-order traversal of BST 'root' and populate a set 'set' with the elements.
    def inorderA(self, root, set):
        if root == None:
            return
        self.inorderA(root.left, set)  # Recursively traverse the left subtree.
        set.add(root.data)  # Add the current node's data to the set.
        # Recursively traverse the right subtree.
        self.inorderA(root.right, set)

    # Function to perform an in-order traversal of BST 'root' and find common elements with the set 'set'.
    def inorderB(self, root, set, ans):
        if root == None:
            return
        # Recursively traverse the left subtree.
        self.inorderB(root.left, set, ans)
        if root.data in set:
            # If the current node's data is in the set, add it to the 'ans' list.
            ans.append(root.data)
        # Recursively traverse the right subtree.
        self.inorderB(root.right, set, ans)

    # Main function to find common elements between two BSTs 'root1' and 'root2'.
    def findCommon(self, root1, root2):
        ans = []  # Initialize an empty list to store common elements.
        s = set()  # Initialize an empty set to store elements from 'root1'.
        # Traverse 'root1' and populate the set 's' with its elements.
        self.inorderA(root1, s)
        # Traverse 'root2' and find common elements with 's'.
        self.inorderB(root2, s, ans)
        return ans  # Return the list of common elements found in both BSTs.


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


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        root1 = buildTree(s)
        s = input()
        root2 = buildTree(s)
        ob = Solution()
        res = ob.findCommon(root1, root2)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
# } Driver Code Ends
