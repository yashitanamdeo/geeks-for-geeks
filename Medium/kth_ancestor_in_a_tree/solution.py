# Problem Statement: https://practice.geeksforgeeks.org/problems/kth-ancestor-in-a-tree/1

# User function Template for python3

from collections import deque


def kthAncestor(root, k, target):

    def dfs(node, acc=[]):
        if node.data == target:
            if len(acc) < k:
                return -1
            else:
                return acc[-k]
        acc.append(node.data)
        result = -1
        if node.left:
            result = dfs(node.left, acc)
        if result == -1 and node.right:
            result = dfs(node.right, acc)
        acc.pop()
        return result

    return dfs(root)


# {
 # Driver Code Starts
# Initial Template for Python 3


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


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
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        k, node = [int(x) for x in input().split()]
        s = input()

        root = buildTree(s)
        print(kthAncestor(root, k, node))
# } Driver Code Ends
