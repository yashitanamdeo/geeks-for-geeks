# Problem Statement: https://practice.geeksforgeeks.org/problems/avl-tree-deletion/1

# User function Template for python3

''' structure of tree node:

class Node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
        self.height=1

'''

from collections import deque


def getHeight(root):
    if not root:
        return 0
    return root.height


def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)


def getMinValueNode(root):
    if root is None or root.left is None:
        return root
    return getMinValueNode(root.left)


def rotateLeft(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(z.right))

    return y


def rotateRight(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    return y


def deleteNode(root, key):
    # code here
    # return root of edited tree

    if not root:
        return root

    elif key < root.data:
        root.left = deleteNode(root.left, key)

    elif key > root.data:
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = getMinValueNode(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)

    if root is None:
        return root

    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    balance = getBalance(root)
    if balance > 1 and getBalance(root.left) >= 0:
        return rotateRight(root)

    if balance < -1 and getBalance(root.right) <= 0:
        return rotateLeft(root)

    if balance > 1 and getBalance(root.left) < 0:
        root.left = rotateLeft(root.left)
        return rotateRight(root)

    if balance < -1 and getBalance(root.right) > 0:
        root.right = rotateRight(root.right)
        return rotateLeft(root)

    return root


# {
 # Driver Code Starts
# Initial Template for Python 3


class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None
        self.height = 1


def setHeights(n):
    if not n:
        return 0
    n.height = 1 + max(setHeights(n.left), setHeights(n.right))
    return n.height


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

    setHeights(root)
    return root


def isBST(n, lower, upper):
    if not n:
        return True

    if n.data <= lower or n.data >= upper:
        return False

    return isBST(n.left, lower, n.data) and isBST(n.right, n.data, upper)


def isBalanced(n):
    if not n:
        return (0, True)

    lHeight, l = isBalanced(n.left)
    rHeight, r = isBalanced(n.right)

    if abs(lHeight - rHeight) > 1:
        return (0, False)

    return (1 + max(lHeight, rHeight), l and r)


def isBalancedBST(root):
    if not isBST(root, -1000000000, 1000000000):
        print("BST voilated, inorder traversal :", end=' ')

    elif not isBalanced(root)[1]:
        print("Unbalanced BST, inorder traversal :", end=' ')

    else:
        return True

    return False


def printInorder(n):
    if not n:
        return
    printInorder(n.left)
    print(n.data, end=' ')
    printInorder(n.right)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)

        n = int(input())
        ip = [int(x) for x in input().split()]

        for i in range(n):
            root = deleteNode(root, ip[i])

            if not isBalancedBST(root):
                break

        if root is None:
            print("null")
        else:
            printInorder(root)
            print()

# } Driver Code Ends
